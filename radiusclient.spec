%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define sdevname %mklibname %{name} -ds

Summary:	Radiusclient library and tools
Name:		radiusclient
Version:	0.3.2
Release:	27
License:	BSD
Group:		System/Libraries
Url:		ftp://ftp.cityline.net/pub/radiusclient/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-am_ac.patch
Patch1:		%{name}-automake-1.13.patch

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
%rename		%{_lib}radius0

%description -n	%{libname}
Libraries required for Radiusclient

%package -n	%{devname}
Summary:	Header files and development documentation for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename		%{_lib}radius-devel

%description -n	%{devname}
Header files and development documentation for %{name}.

%package -n	%{sdevname}
Summary:	Static libraries for %{name}
Group:		Development/C
Requires:	%{devname} = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}
%rename		%{_lib}radius-static-devel

%description -n	%{sdevname}
%{name} static library.

%prep
%setup -q
%apply_patches
autoreconf -fi

%build
%configure2_5x \
	--enable-static \
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
%{_libdir}/libradiusclient.so.%{major}*

%files -n %{devname}
%{_libdir}/libradiusclient.so
%{_includedir}/*

%files -n %{sdevname}
%{_libdir}/libradiusclient.a

