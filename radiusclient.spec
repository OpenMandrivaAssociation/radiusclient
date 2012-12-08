%define	major 0
%define libname	%mklibname radius %{major}
%define develname %mklibname radius -d
%define sdevelname %mklibname radius -d -s

Summary:	Radiusclient library and tools
Name:		radiusclient
Version:	0.3.2
Release:	%mkrel 17
License:	BSD
Group:		System/Libraries
URL:		ftp://ftp.cityline.net/pub/radiusclient/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_ac.patch

%description
Radiusclient is a /bin/login replacement which gets called by a getty
to log in a user and to setup the user's login environment. Normal
login programs just check the login name and password which the user
entered against the local password file (/etc/passwd, /etc/shadow). In
contrast to that Radiusclient also uses the RADIUS protocol to
authenticate the user.

%package -n	%{name}-utils
Summary:	Radiusclient library
Group:          System/Servers

%description -n	%{name}-utils
Radiusclient is a /bin/login replacement which gets called by a getty
to log in a user and to setup the user's login environment. Normal
login programs just check the login name and password which the user
entered against the local password file (/etc/passwd, /etc/shadow). In
contrast to that Radiusclient also uses the RADIUS protocol to
authenticate the user.

%package -n	%{libname}
Summary:	Radiusclient library
Group:          System/Libraries

%description -n	%{libname}
Libraries required for Radiusclient

%package -n	%{develname}
Summary:	Header files and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libradius-devel = %{version}-%{release}
Obsoletes:	%{_lib}radius0-devel < 0.3.2-12

%description -n	%{develname}
Header files and development documentation for %{name}.

%package -n	%{sdevelname}
Summary:	Static libraries for %{name}
Group:		Development/C
Requires:	%{develname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
Obsoletes:	%{_lib}radius0-static-devel < 0.3.2-12

%description -n	%{sdevelname}
%{name} static library.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure2_5x \
    --enable-shadow \
    --enable-scp

%make

%install
%makeinstall_std

%files -n %{name}-utils
%defattr(644,root,root,755)
%doc BUGS CHANGES README* doc/*.html
%dir %{_sysconfdir}/%{name}
%attr(644,root,root) %config(missingok,noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_sbindir}/*

%files -n %{libname}
%defattr(-,root,root)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files -n %{sdevelname}
%defattr(644,root,root,755)
%{_libdir}/lib*.a




%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-15mdv2011.0
+ Revision: 669399
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-14mdv2011.0
+ Revision: 607297
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-13mdv2010.1
+ Revision: 519063
- rebuild

* Sun Oct 04 2009 Funda Wang <fwang@mandriva.org> 0.3.2-12mdv2010.0
+ Revision: 453297
- new devel package policy

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-10mdv2009.1
+ Revision: 317539
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-8mdv2008.1
+ Revision: 179412
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-7mdv2007.0
+ Revision: 134454
- Import radiusclient

* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-7mdv2007.1
- use the %%mkrel macro
- bunzip patches

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.3.2-6mdk
- rebuild

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.2-5mdk
- fix deps

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.3.2-4mdk
- rebuild
- misc spec file fixes

