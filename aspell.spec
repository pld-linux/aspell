Summary:	GNU Aspell is an Open Source spell checker
Summary(pl):	GNU Aspell jest kontrolerem pisowni
Name:		aspell
Version:	0.50.2
Release:	1
Epoch:		2
License:	LGPL
Group:		Applications/Text
Vendor:		Kevin Atkinson <kevina@gnu.org>
Source0:	ftp://ftp.gnu.org/gnu/aspell/%{name}-%{version}.tar.gz
Patch0:		%{name}-libtool.patch
URL:		http://aspell.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildConflicts:	aspell-devel < 0.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libaspell10
Obsoletes:	pspell
Provides:	pspell = %{epoch}:%{version}-%{release}

%description
GNU Aspell is a Free and Open Source spell checker designed to
eventually replace Ispell. It can either be used as a library or as an
independent spell checker. Its main feature is that it does a much
better job of coming up with possible suggestions than just about any
other spell checker out there for the English language, including
Ispell and Microsoft Word. It also has many other technical
enhancements over Ispell such as using shared memory for dictionaries
and intelligently handling personal dictionaries when more than one
Aspell process is open at once.

%description -l pl
GNU Aspell jest kontrolerem pisowni zaprojektowanym tak, by móc
zast±piæ ispella. Dodatkowo zawiera wsparcie dla innych jêzyków ni¿
angielski. Interfejs aspella napisany zosta³ w C++, a interfejsy w
Perlu i C s± aktualnie rozwijane.

%package devel
Summary:	Header files for aspell development
Summary(pl):	Pliki nag³ówkowe dla programistów u¿ywaj±cych aspella
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	libaspell10-devel
Obsoletes:	pspell-devel
Provides:	pspell-devel = %{epoch}:%{version}-%{release}

%description devel
Aspell is an Open Source spell checker. This package contains header
files for aspell development.

%description devel -l pl
Aspell jest kontrolerem pisowni. Ten pakiet zawiera pliki nag³ówkowe
dla programistów u¿ywaj±cych bibliotek aspella.

%package static
Summary:	Static libraries for aspell development
Summary(pl):	Biblioteki statyczne aspella
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	pspell-static
Provides:	pspell-static = %{epoch}:%{version}-%{release}

%description static
Aspell is an Open Source spell checker. This package contains static
aspell libraries.

%description static -l pl
Aspell jest kontrolerem pisowni. Pakiet ten zawiera biblioteki
statyczne aspella.

%prep
%setup -q
%patch0 -p1

%build
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__automake}
%configure \
	--enable-shared \
	--enable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/aspell

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT{%{_bindir}/run-with-aspell,%{_datadir}/aspell/{i,}spell}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README manual/man-html/*.{html,png,css}
%attr(755,root,root) %{_bindir}/a*
%attr(755,root,root) %{_bindir}/w*
%attr(755,root,root) %{_libdir}/lib*.so.*
%attr(755,root,root) %{_libdir}/lib*-common-*.so
%{_datadir}/aspell
%dir %{_libdir}/aspell

%files devel
%defattr(644,root,root,755)
%doc manual/dev-html/*.{html,png,css}
%attr(755,root,root) %{_bindir}/p*
%attr(755,root,root) %{_libdir}/lib*.so
%exclude %{_libdir}/lib*-common-*.so
%{_libdir}/lib*.la
%{_includedir}/pspell
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
