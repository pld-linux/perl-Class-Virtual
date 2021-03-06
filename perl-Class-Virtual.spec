#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Class
%define		pnam	Virtual
Summary:	Class::Virtual Perl module - base class for virtual base classes
Summary(pl.UTF-8):	Moduł Perla Class::Virtual - podstawowa klasa do implementacji podstawowych klas wirtualnych
Name:		perl-Class-Virtual
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c822a4d2ee02795dd2ad0368a6374657
URL:		http://search.cpan.org/dist/Class-Virtual/
BuildRequires:	perl-Class-ISA
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-enum
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Carp-Assert
BuildRequires:	perl-Class-Data-Inheritable
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Virtual is a base class for implementing virtual base classes
(what some people call an abstract class).  Kinda kooky.  It allows
you to explicitly declare what methods are virtual and that must be
implemented by subclasses.  This might seem silly, since your program
will halt and catch fire when an unimplemented virtual method is hit
anyway, but there are some benefits.

%description -l pl.UTF-8
Class::Virtual jest podstawową klasą do implementacji podstawowych
klas wirtualnych (przez niektórych nazywanych klasami abstrakcyjnymi).
Pozwala ona na jawne określenie, które metody są wirtualne i muszą
być zaimplementowane w podklasach. Może się to wydawać głupie, gdyż
program użytkownika i tak stanie (i wznieci ogień) po natrafieniu na
niezaimplementowaną metodę wirtualną, ale rozwiązanie to ma pewne
zalety.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Virtual.pm
%{perl_vendorlib}/Class/Virtually
%{_mandir}/man3/*
