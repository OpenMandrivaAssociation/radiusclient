%define	major 0
%define libname	%mklibname radius %{major}
%define develname %mklibname radius -d
%define sdevelname %mklibname radius -d -s

Summary:	Radiusclient library and tools
Name:		radiusclient
Version:	0.3.2
Release:	%mkrel 13
License:	BSD
Group:		System/Libraries
URL:		ftp://ftp.cityline.net/pub/radiusclient/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_ac.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

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
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files -n %{sdevelname}
%defattr(644,root,root,755)
%{_libdir}/lib*.a


