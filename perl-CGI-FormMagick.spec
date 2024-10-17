%define upstream_name    CGI-FormMagick
%define upstream_version 0.91

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Ness::ted\\)'
%else
%define _provides_exceptions perl(Ness::ted)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	CGI-FormMagick module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
# http://sourceforge.net/projects/formmagick/
Url:		https://search.cpan.org/dist/%{upstream_name}
# http://gd.tuwien.ac.at/platform/linux/e-smith/devel/SRPMS/perl-CGI-FormMagick-0.91-26.src.rpm
Source0:	perl-%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		perl-CGI-FormMagick-0.91-02.mitel_patch
Patch1:		perl-CGI-FormMagick-0.91-03.mitel_patch
Patch2:		perl-CGI-FormMagick-0.91-04.mitel_patch
Patch3:		perl-CGI-FormMagick-0.91-05.mitel_patch
Patch4:		perl-CGI-FormMagick-0.91-06.mitel_patch
Patch5:		perl-CGI-FormMagick-0.91-07.mitel_patch
Patch6:		perl-CGI-FormMagick-0.91-08.mitel_patch
Patch7:		perl-CGI-FormMagick-0.91-09.mitel_patch
Patch8:		perl-CGI-FormMagick-0.91-10.mitel_patch
Patch9:		perl-CGI-FormMagick-0.91-11.mitel_patch
Patch10:	perl-CGI-FormMagick-0.91-12.mitel_patch
Patch11:	perl-CGI-FormMagick-0.91-13.mitel_patch
Patch12:	perl-CGI-FormMagick-0.91-14.mitel_patch
Patch13:	perl-CGI-FormMagick-0.91-15.mitel_patch
Patch14:	perl-CGI-FormMagick-0.91-16.mitel_patch
Patch15:	perl-CGI-FormMagick-0.91-17.mitel_patch
Patch16:	perl-CGI-FormMagick-0.91-18.mitel_patch
Patch17:	perl-CGI-FormMagick-0.91-22.mitel_patch
Patch18:	perl-CGI-FormMagick-0.91-23.mitel_patch
Patch19:	perl-CGI-FormMagick-0.91-24.mitel_patch
Patch20:	perl-CGI-FormMagick-0.91-25.mitel_patch
Patch100:	perl-CGI-FormMagick-0.91-export_names.diff
Patch101:	perl-CGI-FormMagick-0.91-version.diff

BuildRequires:	perl-devel
BuildRequires:	perl(CGI::Persistent)
BuildRequires:	perl(Text::Iconv)
BuildRequires:	perl(Test::Inline)
BuildRequires:	perl-Time-modules
BuildRequires:	perl-Object-Persistence
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(Text::Template)
BuildRequires:	perl(Class::ParamParser)
BuildRequires:	perl(Mail::RFC822::Address)
BuildArch:	noarch

%description
FormMagick is a toolkit for easily building fairly complex form-based
web applications.  It allows the developer to specify the structure of a
multi-page "wizard" style form using XML, then display that form using
only a few lines of Perl.

%prep
%setup -q -n perl-%{upstream_name}-%{upstream_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1

%patch100 -p1
%patch101 -p0

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
# it's not that make test fails some test: it just doesn't work
#make test

%install
%makeinstall_std

%files
%doc Changes README doc COPYING INSTALL examples
%{perl_vendorlib}/CGI/FormMagick
%{perl_vendorlib}/CGI/FormMagick.pm
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.910.0-2mdv2011.0
+ Revision: 680688
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-1mdv2011.0
+ Revision: 402998
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.91-6mdv2009.0
+ Revision: 255772
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-4mdv2008.1
+ Revision: 136904
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.91-3mdv2007.0
+ Revision: 73386
- bunzip patches
- import perl-CGI-FormMagick-0.91-3mdk

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.91-3mdk
- Fix SPEC Using perl Policies
	- BuildRequires

* Sun Nov 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.91.2mdk
- oops!, P100 was a little wrong, fixed...

* Sun Nov 06 2005 Oden Eriksson <oeriksson@mandriva.com> 0.91.1mdk
- use source and patches from e-smith
- added P100 to make the auto dep/req work
- added P101 to make it report correct version
- use the macromdv2007.1- rule out some useless auto provides

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.89-1mdk
- initial Mandriva package

