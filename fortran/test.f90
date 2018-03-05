program basictest
implicit none

logical, parameter :: jf(50) = .true.
integer, parameter :: jmag = 1, iyyyy=1980,mmdd=0321,dhour=12
real, parameter :: glat=0., glon=0.
real,parameter :: altkm(1) = 130.
integer,parameter ::  Nalt = size(altkm)
character(*), parameter :: datadir = 'data/'

real :: oarr(100), outf(30,Nalt)


call IRI_SUB(JF,JMAG,glat,glon,IYYYY,MMDD,DHOUR+25, altkm,Nalt,datadir,OUTF,OARR)

print '(A,ES10.3,A,F5.1,A)','NmF2 ',oarr(1),' [m^-3]     hmF2 ',oarr(2),' [km] '
print '(A,F10.3,A,I3,A,F10.3)','F10.7 ',oarr(41), ' Ap ',int(oarr(51)),' B0 ',oarr(10)

end program