program basictest
implicit none

logical, parameter :: jf(50) = .true.
integer, parameter :: jmag = 1, iyyyy=1980,mmdd=0321,dhour=12
real, parameter :: glat=0., glon=0.
real,parameter :: altkm(1) = 130.
integer,parameter ::  Nalt = size(altkm)
character(*), parameter :: datadir = 'data/'

real :: oarr(100), outf(30,Nalt)
integer :: i

do i=1,10
    call IRI_SUB(JF,JMAG,glat,glon,IYYYY,MMDD,DHOUR+25, altkm,Nalt,datadir,OUTF,OARR)

    print '(A,ES10.3,A,F5.1,A)','NmF2 ',oarr(1),' [m^-3]     hmF2 ',oarr(2),' [km] '
    print '(A,F10.3,A,I3,A,F10.3)','F10.7 ',oarr(41), ' Ap ',int(oarr(51)),' B0 ',oarr(10)
enddo

end program


! logical, parameter :: jf(50) = .true.
! integer, parameter :: jmag = 1, iyyyy=1980,mmdd=0321,dhour=12
! real, parameter :: glat=0., glon=0.
! real,parameter :: altkm(1) = 130.

! ** IRI parameters are being calculated ***
!Ne: IRI-2001 for Topside
!Ne, foF2: CCIR model is used.
!Ne: B0,B1 Bil-2000
!Ne, foF1: probability function used.
!Ne, D: IRI1990
!Ne, foF2: storm model included
!Ion Com.: DS-95 & DY-85
!Te: Aeros/AE/ISIS model
!Auroral boundary model on
!Ne, foE: storm model on
! NmF2  1.362E+12 [m^-3]     hmF2 327.5 [km]
! F10.7    162.400 Ap  18 B0     88.054
