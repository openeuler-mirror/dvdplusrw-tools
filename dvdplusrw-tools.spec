Name:           dvd+rw-tools
Version:        7.1
Release:        34
Summary:        Application to master the Blu-ray Disc and DVD media
License:        GPLv2
URL:            http://fy.chalmers.se/~appro/linux/DVD+RW/
Source0:        http://fy.chalmers.se/~appro/linux/DVD+RW/tools/dvd+rw-tools-7.1.tar.gz
Source1:        index.html
Patch0000:      0000-dvd+rw-tools-7.0.manpatch
Patch0001:      0001-dvd+rw-tools-7.0-wexit.patch
Patch0002:      0002-dvd+rw-tools-7.0-glibc2.6.90.patch
Patch0003:      0003-dvd+rw-tools-7.0-reload.patch
Patch0004:      0004-dvd+rw-tools-7.0-wctomb.patch
Patch0005:      0005-dvd+rw-tools-7.0-dvddl.patch
Patch0006:      0006-dvd+rw-tools-7.1-noevent.patch
Patch0007:      0007-dvd+rw-tools-7.1-lastshort.patch
Patch0008:      0008-dvd+rw-tools-7.1-format.patch
Patch0009:      0009-dvd+rw-tools-7.1-bluray_srm+pow.patch
Patch0010:      0010-dvd+rw-tools-7.1-bluray_pow_freespace.patch
Patch0011:      0011-dvd+rw-tools-7.1-sysmacro-inc.patch
Patch0012:      support-specify-cc.patch

BuildRequires:  gcc-c++ kernel-headers m4
Requires:       genisoimage

%description
As implied/already mentioned - to master the Blu-ray Disc and DVD media,
both +RW/+R and -R[W].

%package        help
Summary:        Help docs for dvd+rw-tools
Buildarch:      noarch
Requires:       man info

%description    help
This package contains the help docs for dvd+rw-tools

%prep
%autosetup -n dvd+rw-tools-7.1 -p1

install -m 644 %{SOURCE1} index.html

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export LDFLAGS="$RPM_LD_FLAGS"
%if "%toolchain" == "clang"
    CFLAGS="$CFLAGS -Wno-error=reserved-user-defined-literal"
    CXXFLAGS="$CXXFLAGS -Wno-error=reserved-user-defined-literal"
%endif

%make_build WARN="-DDEFAULT_BUF_SIZE_MB=16 -DRLIMIT_MEMLOCK"

%install
%if "%toolchain" == "clang"
    CFLAGS="$CFLAGS -Wno-error=reserved-user-defined-literal"
    CXXFLAGS="$CXXFLAGS -Wno-error=reserved-user-defined-literal"
%endif
%makeinstall

%pre

%preun

%post

%postun

%files
%defattr(-,root,root)
%doc index.html LICENSE
%{_bindir}/*

%files help
%{_mandir}/man1/*.1*

%changelog
* Fri Apr 21 2023 jammyjellyfish <jammyjellyfish255@outlook.com> - 7.1-34
- Fix clang build error

* Tue Oct 26 2021 chenchen <chen_aka_jan@163.com> - 7.1-33
- change the spec file name to be the same as the repo name

* Wed Nov 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 7.1-32
- Package init
