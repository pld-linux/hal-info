%define		snap	20070618
Summary:	Device information for HAL
Summary(pl.UTF-8):	Informacje o urządzeniach dla HAL-a
Name:		hal-info
Version:	0.0
Release:	0.%{snap}.1
License:	AFL v2.1 or GPL v2
Group:		Libraries
Source0:	http://people.freedesktop.org/~david/dist/%{name}-%{snap}.tar.gz
# Source0-md5:	c7005ccb1765d8359fd2348350770495
Patch0:		hal-samsung_yp_z5.patch
URL:		http://freedesktop.org/Software/hal
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
Requires:	hal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hal-info contains device information for HAL.

%description -l pl.UTF-8
hal-info zawiera informacje o urządzeniach dla HAL-a.

%prep
%setup -q -n %{name}-%{snap}
%patch0 -p1

[ -f VERSION ] && exit 1
echo %{snap} > VERSION

%build
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
