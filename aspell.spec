%define	name	aspell
%define	version	.27.2
%define	release	2
%define	serial	1

Summary:	Aspell is an Open Source spell checker.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Serial:		%{serial}
Copyright:	LGPL
Group:		Utilities/Text
URL:		http://metalab.unc.edu/kevina/aspell
Vendor:		Kevin Atkinson <kevinatk@home.com>
Source:		%{name}-%{version}.tar.gz
Distribution:	Freshmeat RPMs
Packager:	Ryan Weaver <ryanw@infohwy.com>
BuildRoot:	/tmp/%{name}-%{version}

%description
 Aspell is an Open Source spell checker designed to eventually replace
 Ispell. Its main feature is that it does a much better job of coming
 up with possible suggestions than Ispell does. In fact recent tests
 shows that it even does better than Microsoft Word 97's spell checker
 in some cases. In addition it has both compile time and run time
 support for other non English languages. Aspell also doubles as a
 powerful C++ library with C and Perl interfaces in the works.

%package	devel
Summary:	Static Libraries and header files for aspell
Group:		Development/Libraries
Serial:		%{serial}
%description	devel
 Aspell is an Open Source spell checker.

 Static Libraries and header files for aspell

%prep
%setup -q

cp -p /usr/include/g++/stl_rope.h .
patch <misc/stl_rope-30.diff

./configure --prefix=/usr --enable-static

%build
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-strip

cp -pr $RPM_BUILD_ROOT/usr/doc/aspell .

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README TODO aspell/*
/usr/bin/aspell
/usr/bin/run-with-aspell
/usr/lib/aspell
/usr/lib/libaspell.so.*

%files		devel
%defattr(-,root,root)
/usr/include/aspell
/usr/lib/libaspell.a
/usr/lib/libaspell.la
/usr/lib/libaspell.so

%changelog
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
