Summary:	Aspell is an Open Source spell checker.
Name:		aspell
Version:	.27.2
Release:	3
Serial:		1
Copyright:	LGPL
Group:		Utilities/Text
Group(pl):	Narzêdzia/Tekst
URL:		http://metalab.unc.edu/kevina/aspell
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source:		%{name}-%{version}.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root

%description
 Aspell is an Open Source spell checker designed to eventually replace
 Ispell. Its main feature is that it does a much better job of coming
 up with possible suggestions than Ispell does. In fact recent tests
 shows that it even does better than Microsoft Word 97's spell checker
 in some cases. In addition it has both compile time and run time
 support for other non English languages. Aspell also doubles as a
 powerful C++ library with C and Perl interfaces in the works.

%package	devel
Summary:	Libraries and header files for aspell development
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Serial:		%{serial}
Requires:	%{name} = %{version}

%description	devel
 Aspell is an Open Source spell checker.

 Libraries and header files for aspell development

%package	static
Summary:	Static Libraries for aspell development
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Serial:		%{serial}
Requires:	%{name}-devel = %{version}

%description	static
 Aspell is an Open Source spell checker.

 Static Libraries for aspell development

%prep
%setup -q

cp -p /usr/include/g++/stl_rope.h .
patch <misc/stl_rope-30.diff

%build
%configure --enable-static
make

%install
rm -rf $RPM_BUILD_ROOT
install -p $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install-strip

cp -pr $RPM_BUILD_ROOT/usr/doc/aspell .

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO aspell/*
%attr(755,root,root) /usr/bin/aspell
%attr(755,root,root) /usr/bin/run-with-aspell
/usr/lib/aspell
/usr/lib/libaspell.so.*.*

%files	devel
%defattr(644,root,root,755)
%attr(755,root,root) /usr/lib/libaspell.so
/usr/include/aspell
/usr/lib/libaspell.la

%files static
%defattr(644,root,root,755)
/usr/lib/libaspell.a

%changelog
* Fri Apr 30 1999 Artur Frysiak <wiget@pld.org.pl>
  [.27.2-3]
- added static subpackage
- full %%attr description
- partial pl translation

* Tue Mar  2 1999 Ryan Weaver <ryanw@infohwy.com>
  [aspell-.27.2-2]
- Changes from .27.1 to .27.2 (Mar 1, 1999)
- Fixed a major bug that caused aspell to dump core when used
  without any arguments
- Fixed another major bug that caused aspell to do nothing when used
  in interactive mode.
- Added an option to exit in Aspell's interactive mode.
- Removed some old documentation files from the distribution.
- Minor changes on to the section on using Aspell with egcs.
- Minor changes to remove -Wall warnings.
