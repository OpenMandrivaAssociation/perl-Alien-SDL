%define upstream_name    Alien-SDL
%define upstream_version 1.423

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Building, finding and using SDL binaries
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: SDL-devel
BuildRequires: perl(Archive::Extract)
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(Archive::Zip)
BuildRequires: perl(Capture::Tiny)
BuildRequires: perl(Digest::SHA)
BuildRequires: perl(ExtUtils::CBuilder)
BuildRequires: perl(File::Fetch)
BuildRequires: perl(File::Find)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::ShareDir)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Which)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Text::Patch)
Obsoletes: %{name} < %{version}-%{release}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Please see the Alien manpage for the manifesto of the Alien namespace.

In short 'Alien::SDL' can be used to detect and get configuration settings
from an installed SDL and related libraries. Based on your platform it
offers the possibility to download and install prebuilt binaries or to
build SDL & co. from source codes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL --with-sdl-config='%{_bindir}/sdl-config' installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*


