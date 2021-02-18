  program main

!=======================================================================
! read_JMA_SNOWD.f90
! 気象庁の解析積雪深を読み込むプログラム
! written by Maki OKADA(2019.11.18)
!=======================================================================
  implicit none

!---------!---------!---------!---------!---------!---------!---------72
! Constatnt
  integer(kind=4),parameter :: imiss=9999
  real(kind=4),parameter    :: rmiss=9999.0

  integer(kind=4),parameter :: nx=512,ny=560
  integer(kind=4),parameter :: ndata=nx*ny
  integer(kind=4),parameter :: npnt=500

! Time
  integer(kind=4) :: jj
  integer(kind=4) :: idt(5) !UTC
  integer(kind=4) :: jdt(5) !JST
  character       :: cdt*12

! Point
  integer(kind=4) :: jx,jy
  real(kind=4)    :: rlon_d(ndata),rlat_d(ndata)
  real(kind=4)    :: rlon_f(nx,ny),rlat_f(nx,ny)
  real(kind=4)    :: rdx,rdy
  integer         :: jpnt,nmax,ix,iy
  integer         :: ipnt,imk,ilat,ilon
  integer         :: iamd(npnt)
  real            :: rlat(npnt),rlon(npnt)
  real            :: rval(npnt)

! Element
  real, allocatable :: rdat(:,:)     !input data
  real              :: rsdp0(nx,ny)
  real              :: rsdp(nx,ny)

  integer         :: ii,imax
  real            :: rsdp_d(ndata)

! File
  character :: cdir*100
  character :: cfln*100
  integer   :: ios
!---------!---------!---------!---------!---------!---------!---------72
!=======================================================================
! get arg
!=======================================================================
      call getarg(1,cdir)

!=======================================================================
! set time
!=======================================================================
      open(21,file='../src/ini_utc.dat',status='old') !Initial Time
      read(21,'(i4,4i2)')(idt(jj),jj=1,5)
      close(21)
      call dtinc(idt,jdt,4,9) !UTC -> JST
      write(cdt,'(i4,4i2.2)')idt

!=======================================================================
! read binary
!=======================================================================
! 初期化
      allocate(rdat(nx,ny))
      do jy=1,ny; do jx=1,nx
         rsdp0(jx,jy)=rmiss
         rsdp(jx,jy)=rmiss
      end do ; end do

! 読み込みファイル名決定
      cfln=trim(cdir)//'/dat/Z__C_RJTD_'//cdt//'00_SRF_GPV_Gll5km_Psdlv_ANAL_grib2.dat'
      write(6,*)cfln

! データ取得
      open(20,file=cfln,status='old',form='unformatted' &
          ,access='direct',recl=4*nx*ny,err=9999)
      read(20,rec=1) rdat

! エンディアン変換(big-endian)
      do jy=1,ny
      do jx=1,nx
         call bytswp(rdat(jx,jy),rsdp0(jx,jy))
!!         if(rsdp0(jx,jy).ne.rmiss)then
            rsdp(jx,jy)=rsdp0(jx,jy)*100
!!         end if !rsdp0
      end do !jx
      end do !jy

 9999 close(20)

!=======================================================================
! 出力
!=======================================================================
! メッシュごとの緯度経度
      rdx=(150.0-118.0)/real(nx)
      rdy=(48.0-20.0)/real(ny)

      ii=0
      do jy=1,ny
      do jx=1,nx
         rlon_f(jx,jy)=118.0+ rdx*real(jx-1)
         rlat_f(jx,jy)= 20.0+ rdy*real(jy-1)
         ii=ii+1
         rlon_d(ii)=118.0+ rdx*real(jx-1)
         rlat_d(ii)= 20.0+ rdy*real(jy-1)
         rsdp_d(ii)=rsdp(jx,jy)
      end do !jx
      end do !jy
      imax=ii

! GMT用バイナリ出力
      open(31,file=trim(cdir)//'/dat/sdp.bin',status='unknown'&
          ,access='direct',form='unformatted',recl=3*4*nx*ny)
      write(31,rec=1)(rlon_d(ii),rlat_d(ii),rsdp_d(ii),ii=1,imax)
      close(31)

! テキスト出力
      open(30,file=trim(cdir)//'/dat/sdp.txt',status='unknown')
      do jy=1,ny; do jx=1,nx
         if(rsdp0(jx,jy).ne.rmiss)then
            write(30,'(2f10.4,i8)') &
                  rlon_f(jx,jy),rlat_f(jx,jy),nint(rsdp(jx,jy))
         end if
      end do ; end do
      close(30)

!=======================================================================
! ポイント出力
!=======================================================================
! 地点リスト読込
      jpnt=1
      open(40,file='../tbl/F0270000.TBL',status='old')
      do 
      read(40,'(i5,1x,i1,1x,i5,1x,i6)',iostat=ios)ipnt,imk,ilat,ilon
      if(ios<0)exit
      if(imk.eq.9)then
         iamd(jpnt)=ipnt
         rlat(jpnt)=real(ilat)/1000.0
         rlon(jpnt)=real(ilon)/1000.0
         jpnt=jpnt+1
      end if
      end do
      close(20)
      nmax=jpnt-1

      open(41,file=trim(cdir)//'/dat/sdp_pnt.txt',status='unknown')
      rdx=(150.0-118.0)/real(nx)
      rdy=(48.0-20.0)/real(ny)
      do jpnt=1,nmax
         ix=1+(rlon(jpnt)-118.0)/rdx
         iy=1+(rlat(jpnt)-20.0)/rdy
         rval(jpnt)=rsdp(ix,iy)
      end do
      write(41,'(12x,324i7)')(iamd(jpnt),jpnt=1,324)
      write(41,'(12x,324f7.1)')(rval(jpnt),jpnt=1,324)
      close(41)

      deallocate(rdat)
!=======================================================================
      end program main
