%define upstream_name    Alien-SDL
%define upstream_version 1.436

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Building, finding and using SDL binaries
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	SDL-devel
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
BuildArch:	noarch

%description
Please see the Alien manpage for the manifesto of the Alien namespace.

In short 'Alien::SDL' can be used to detect and get configuration settings
from an installed SDL and related libraries. Based on your platform it
offers the possibility to download and install prebuilt binaries or to
build SDL & co. from source codes.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
echo 1 | %{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc META.yml Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.427.0-3mdv2012.0
+ Revision: 765049
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed Jun 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.427.0-1
+ Revision: 686618
- update to new version 1.427

* Mon Apr 25 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.426.0-1
+ Revision: 658378
- new version 1.426

* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 1.425.0-2
+ Revision: 640732
- rebuild to obsolete old packages

* Fri Feb 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.425.0-1
+ Revision: 635782
- update to new version 1.425

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.424.0-1
+ Revision: 635487
- update to new version 1.424

* Thu Jan 27 2011 Shlomi Fish <shlomif@mandriva.org> 1.423.0-1
+ Revision: 633245
- Upgrade to 1.423, and now using --with-sdl-config

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.421

* Mon Aug 23 2010 Jérôme Quelin <jquelin@mandriva.org> 1.413.0-1mdv2011.0
+ Revision: 572269
- update to 1.413

  + Funda Wang <fwang@mandriva.org>
    - New version 1.412
    - drop unneeded BRs
    - rebuild

* Thu Apr 08 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-2mdv2010.1
+ Revision: 533041
- rebuild with pango support

* Wed Apr 07 2010 Jérôme Quelin <jquelin@mandriva.org> 1.200.0-1mdv2010.1
+ Revision: 532719
- import perl-Alien-SDL


* Wed Apr 07 2010 cpan2dist 1.2-1mdv
- initial mdv release, generated with cpan2dist
