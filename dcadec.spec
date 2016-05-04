# globals for dcadec-0.2.0-20160504-df18a5f.tar
%global gitdate 20160504
%global gitversion df18a5f
%global snapshot %{gitdate}-%{gitversion}
%global gver .%{gitdate}git%{gitversion}

Name:           dcadec
Version:        0.2.0
Release:	2%{?gver}%{dist}
Summary:        DTS Coherent Acoustics decoder with support for HD extensions
License:        LGPLv2
Group: 		Applications/Multimedia
Url:            https://github.com/foo86/dcadec
Source:		%{name}-%{version}-%{snapshot}.tar
Source1: 	%{name}-snapshot.sh
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:	git
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       %{name}-libs = %{version}-%{release}

%description
Free DTS Coherent Acoustics decoder with support for HD extensions.

Supported features:
    Decoding of standard DTS core streams with up to 5.1 channels
    Decoding of DTS-ES streams with discrete back channel
    Decoding of High Resolution streams with up to 7.1 channels 
and extended bitrate
    Decoding of 96/24 core streams
    Lossless decoding of Master Audio streams with up to 7.1 channels, 
    192 kHz
    Downmixing to stereo and 5.1 using embedded coefficients

Features not implemented:
    Decoding of DTS Express streams
    Applying dynamic range compression and dialog normalization

%package     libs
Summary:        Shared library for dcadec
Group:          System/Libraries

%description libs
DTS Coherent Acoustics decoder with support for HD extensions

%package     devel
Summary:        Header files and static library for lib%{name}
Group:          Development/Libraries/C and C++
Requires:      %{name}-libs = %{version}-%{release}

%description devel
DTS Coherent Acoustics decoder with support for HD extensions

%prep
%setup -q

%build
export CFLAGS="-fPIC %{optflags}"
make CONFIG_SHARED=1 %{?_smp_mflags}


%install
PREFIX=/usr LIBDIR=%{_libdir} CONFIG_SHARED=1 %make_install
cp -af libdcadec/libdcadec.so.0 %{buildroot}%{_libdir}/
chmod a+x %{buildroot}/%{_libdir}/lib%{name}.so.0.1.0

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING.LGPLv2.1 README.md
%{_bindir}/%{name}

%files libs
%defattr(-,root,root)
%doc COPYING.LGPLv2.1 README.md
%{_libdir}/lib%{name}.so.0
%{_libdir}/lib%{name}.so.0.1.0

%files devel
%defattr(-,root,root)
%doc COPYING.LGPLv2.1 README.md
%{_includedir}/lib%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog

* Wed May 04 2016 David Vásquez <davidjeremias82 at gmail dot com> - 0.2.0-20160504-df18a5f-2
- Updated to 0.2.0-20160504-df18a5f
- Solved rpmlint issues

* Thu Mar 03 2016 David Vásquez <davidjeremias82 at gmail dot com> - 0.2.0-1
- Initial build
