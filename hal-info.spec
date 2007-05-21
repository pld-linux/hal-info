%define		snap	20070521
Summary:	Device information for HAL
Name:		hal-info
Version:	0.0
Release:	0.%{snap}.1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	db0afd4050dc0205ca88cef03722dfd0
URL:		http://freedesktop.org/Software/hal
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
Requires:	hal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hal-info contains device information for HAL.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_datadir}/hal/fdi/information/10freedesktop/*.fdi
%{_datadir}/hal/fdi/preprobe/10osvendor/*.fdi
