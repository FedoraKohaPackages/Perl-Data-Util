Name:           perl-Data-Util
Version:        0.64
Release:        1%{?dist}
Summary:        Selection of utilities for data and data types
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-Util/
Source0:        http://www.cpan.org/authors/id/G/GF/GFUJI/Data-Util-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 1:5.8.1
BuildRequires:  perl-Module-Install-XSUtil
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Test::Exception) >= 0.27
BuildRequires:  perl(Test::More) >= 0.62
BuildRequires:  perl(XSLoader) >= 0.02
Requires:       perl(XSLoader) >= 0.02
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Data::Util::PurePerl)

%description
This module provides utility functions for data and data types, including
functions for subroutines and symbol table hashes (stashes).

%prep
%setup -q -n Data-Util-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Thu Jun 16 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.64-1
- new package built with tito

* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.63-1
- Specfile autogenerated by cpanspec 1.78.
