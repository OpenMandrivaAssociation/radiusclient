%define	major 0
%define libname	%mklibname radius %{major}

Summary:	Radiusclient library and tools
Name:		radiusclient
Version:	0.3.2
Release:	%mkrel 7
License:	BSD
Group:		System/Libraries
URL:		ftp://ftp.cityline.net/pub/radiusclient/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_ac.patch
BuildRequires:	libtool
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
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

%package -n	%{libname}-devel
Summary:	Header files and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel libradius-devel

%description -n	%{libname}-devel
Header files and development documentation for %{name}.

%package -n	%{libname}-static-devel
Summary:	Static libraries for %{name}
Group:		Development/C
Requires:	%{libname}-devel = %{version}-%{release}

%description -n	%{libname}-static-devel
%{name} static library.

%prep

%setup -q
%patch0 -p1

%build
rm -rf missing configure
export WANT_AUTOCONF_2_5=1
libtoolize --copy --force; aclocal-1.7; autoconf; automake-1.7 --add-missing

%configure2_5x \
    --enable-shadow \
    --enable-scp

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

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

%files -n %{libname}-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files -n %{libname}-static-devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a


