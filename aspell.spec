%define		ver	.33.7.1

Summary:	Aspell is an Open Source spell checker
Summary(pl):	Aspell jest kontrolerem pisowni
Name:		aspell
Version:	0%{ver}
Release:	2
Epoch:		1
License:	LGPL
Group:		Applications/Text
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/aspell/%{name}-%{ver}.tar.gz
Patch0:		ftp://ftp.sourceforge.net/pub/sourceforge/aspell/%{name}-.33-fix2.diff
Patch1:		%{name}-noinstalled.patch
Patch2:		%{name}-amfix.patch
URL:		http://aspell.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pspell-devel
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
ispella. Dodatkowo zawiera wsparcie dla innych jêzyków ni¿ angielski.
Interfejs aspella napisany zosta³ w C++, a interfejsy w Perlu i C s±
aktualnie rozwijane.

%package devel
Summary:	Header files for aspell development
Summary(pl):	Pliki nag³ówkowe dla programistów u¿ywaj±cych aspella
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Aspell is an Open Source spell checker. This package contains header
files for aspell development.

%description -l pl devel
Aspell jest kontrolerem pisowni. Ten pakiet zawiera pliki nag³ówkowe
dla programistów u¿ywaj±cych bibliotek aspella.

%package static
Summary:	Static libraries for aspell development
Summary(pl):	Biblioteki statyczne aspella
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Aspell is an Open Source spell checker. This package contains static
aspell libraries.

%description -l pl static
Aspell jest kontrolerem pisowni. Pakiet ten zawiera biblioteki
statyczne aspella.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f --foreign
%configure \
	--enable-shared \
	--enable-static \
	--enable-dict-dir=%{_datadir}/aspell

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf aspell $RPM_BUILD_ROOT%{_bindir}/ispell
rm -rf $RPM_BUILD_ROOT%{_prefix}/{bin/run-with-aspell,share/aspell/ispell}

gzip -9nf manual/manual2.lyx manual/man-text/*.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc manual/{*,man-text/*.txt}.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libaspell.so.*.*
%attr(755,root,root) %{_libdir}/libpspell_aspell.so.*.*
%attr(755,root,root) %{_libdir}/libpspell_aspell.la
%{_datadir}/aspell
%{_datadir}/pspell/*

%files	devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaspell.so
%attr(755,root,root) %{_libdir}/libaspell.la
%{_includedir}/aspell

%files static
%defattr(644,root,root,755)
%{_libdir}/libaspell.a
