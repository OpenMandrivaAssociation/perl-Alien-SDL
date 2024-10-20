%define upstream_name    Alien-SDL
%define upstream_version 1.446

Summary:	Building, finding and using SDL binaries


Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	perl(Archive::Extract)
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl(File::Fetch)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::Which)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Text::Patch)
BuildRequires:  perl(JSON::PP)

%description
Please see the Alien manpage for the manifesto of the Alien namespace.

In short 'Alien::SDL' can be used to detect and get configuration settings
from an installed SDL and related libraries. Based on your platform it
offers the possibility to download and install prebuilt binaries or to
build SDL & co. from source codes.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
echo 1 | %{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot}

%files
%doc META.yml Changes README LICENSE
%{_mandir}/man3/*
%{_bindir}/*
%{perl_vendorlib}/*



