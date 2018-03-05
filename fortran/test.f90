program basictest
implicit none

logical, parameter :: jf(50) = .true.
integer, parameter :: jmag = 1, iyyyy=2012,mmdd=0821,dhour=12
real, parameter :: glat=40., glon=-100.
real,parameter :: altkm(1) = 130.
integer,parameter ::  Nalt = size(altkm)
character(*), parameter :: datadir = 'data/'

real :: oarr(100), outf(30,Nalt)


call IRI_SUB(JF,JMAG,glat,glon,IYYYY,MMDD,DHOUR+25, altkm,Nalt,datadir,OUTF,OARR)


end program