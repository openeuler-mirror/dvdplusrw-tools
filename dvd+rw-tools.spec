Name:           dvd+rw-tools
Version:        7.1
Release:        31
Summary:        Application to master the Blu-ray Disc and DVD media
License:        GPLv2
URL:            http://fy.chalmers.se/~appro/linux/DVD+RW/
Source0:        http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-%{version}.tar.gz
Source1:        index.html
Patch0:         0000-dvd+rw-tools-7.0.manpatch
Patch1:         0001-dvd+rw-tools-7.0-wexit.patch
Patch2:         0002-dvd+rw-tools-7.0-glibc2.6.90.patch
Patch3:         0003-dvd+rw-tools-7.0-reload.patch
Patch4:         0004-dvd+rw-tools-7.0-wctomb.patch
Patch5:         0005-dvd+rw-tools-7.0-dvddl.patch
Patch6:         0006-dvd+rw-tools-7.1-noevent.patch
Patch7:         0007-dvd+rw-tools-7.1-lastshort.patch
Patch8:         0008-dvd+rw-tools-7.1-format.patch
Patch9:         0009-dvd+rw-tools-7.1-bluray_srm+pow.patch
Patch10:        0010-dvd+rw-tools-7.1-bluray_pow_freespace.patch
Patch11:        0011-dvd+rw-tools-7.1-sysmacro-inc.patch

BuildRequires:  gcc gcc-c++ kernel-headers m4
Requires:       genisoimage

%description
As implied/already mentioned - to master the Blu-ray Disc and DVD media,
both +RW/+R and -R[W].

%package_help

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p0
%patch5 -p0
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

install -m 644 %{SOURCE1} index.html

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export LDFLAGS="$RPM_LD_FLAGS"
make WARN="-DDEFAULT_BUF_SIZE_MB=16 -DRLIMIT_MEMLOCK" %{?_smp_mflags}

%install
%makeinstall

%pre

%preun

%post

%postun

%files
%defattr(-,root,root)
%license LICENSE
%doc index.html
%{_bindir}/*

%files help
%{_mandir}/man1/*.1*

%changelog
* Wed Nov 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.1-31
- Package init
