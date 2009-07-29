%define upstream_name    CGI-FormMagick
%define upstream_version 0.91

%define _provides_exceptions perl(Ness::ted)

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	CGI-FormMagick module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
# http://sourceforge.net/projects/formmagick/
Url:		http://search.cpan.org/dist/%{upstream_name}
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

BuildRequires:  perl(CGI::Persistent)
BuildRequires:  perl(Text::Iconv)
BuildRequires:  perl(Test::Inline)
BuildRequires:	perl-Time-modules
BuildRequires:  perl-Object-Persistence
BuildRequires:  perl(XML::Parser)
BuildRequires:	perl(Text::Template)
BuildRequires:  perl(Class::ParamParser)
BuildRequires:  perl(Mail::RFC822::Address)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
# it's not that make test fails some test: it just doesn't work
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README doc COPYING INSTALL examples
%{perl_vendorlib}/CGI/FormMagick
%{perl_vendorlib}/CGI/FormMagick.pm
%{_mandir}/*/*
