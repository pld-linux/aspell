Summary:	Aspell is an Open Source spell checker.
Summary(pl):	Aspell jest kontrolerem pisowni.
Name:		aspell
Version:	.27.2
Release:	3
Serial:		1
License:	LGPL
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narzêdzia/Tekst
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source0:	http://metalab.unc.edu/kevina/aspell/%{name}-%{version}.tar.gz
URL:		http://metalab.unc.edu/kevina/aspell/
BuildRequires:	libstdc++-devel
Provides:	ispell
Obsoletes:	ispell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aspell is an Open Source spell checker designed to eventually replace
Ispell. Its main feature is that it does a much better job of coming
up with possible suggestions than Ispell does. In fact recent tests
shows that it even does better than Microsoft Word 97's spell checker
in some cases. In addition it has both compile time and run time
support for other non English languages. Aspell also doubles as a
powerful C++ library with C and Perl interfaces in the works.

%description -l pl
Aspell jest kontrolerem pisowni zaprojektowanym tak, by móc zast±piæ
ispell'a. Dodatkowo zawiera wsparcie dla innych jêzyków ni¿ angielski.
Interfejs aspella napisany zosta³ w C++, a interfejsy w Perlu i C s±
aktualnie rozwijane.

%package devel
Summary:	Libraries and header files for aspell development
Summary(pl):	Biblioteki i pliki nag³ówkowe dla developerów aspella
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Serial:		%{serial}
Requires:	%{name} = %{version}

%description devel
Aspell is an Open Source spell checker.

Libraries and header files for aspell development

%description -l pl devel
Aspell jest kontrolerem pisowni. Pakiet ten zawiera biblioteki i pliki
nag³ówkowe dla developerów aspella.

%package static
Summary:	Static Libraries for aspell development
Summary(pl):	Biblioteki statyczne dla developerów aspella
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Serial:		%{serial}
Requires:	%{name}-devel = %{version}

%description static
Aspell is an Open Source spell checker.

Static Libraries for aspell development

%description -l pl static
Aspell jest kontrolerem pisowni. Pakiet ten zawiera biblioteki
statyczne dla developerów aspella.

%prep
%setup -q

cp -p %{_includedir}/g++/stl_rope.h .
patch <misc/stl_rope-30.diff

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
--prefix=%{_prefix} \
	--libdir=%{_datadir} \
	--enable-shared \
	--enable-static
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdatadir=%{_datadir}/aspell \
	libdir=%{_libdir}

#cp -pr $RPM_BUILD_ROOT%{_prefix}/doc/aspell .

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*
strip $RPM_BUILD_ROOT%{_bindir}/* || :

ln -sf aspell $RPM_BUILD_ROOT%{_bindir}/ispell
rm -rf $RPM_BUILD_ROOT%{_prefix}/{bin/run-with-aspell,share/aspell/ispell}

gzip -9nf manual/manual2.lyx manual/man-text/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO manual/{*,man-text/*.txt}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/aspell
%{_libdir}/libaspell.so.*.*

%files	devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaspell.so
%{_includedir}/aspell
%{_libdir}/libaspell.la

%files static
%defattr(644,root,root,755)
%{_libdir}/libaspell.a

%define date	%(LC_ALL="C" date +"%a %b %d %Y"`)
