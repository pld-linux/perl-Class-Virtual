%include	/usr/lib/rpm/macros.perl
%define		pdir	Class
%define		pnam	Virtual
Summary:	Class::Virtual Perl module - base class for virtual base classes
Summary(pl):	Modu³ Perla Class::Virtual - podstawowa klasa do implementacji podstawowych klas wirtualnych
Name:		perl-Class-Virtual
Version:	0.04
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3c1102f97a50904da1240f3f67446e4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Class-ISA
BuildRequires:	perl-enum
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::Virtual is a base class for implementing virtual base classes
(what some people call an abstract class).  Kinda kooky.  It allows
you to explicitly declare what methods are virtual and that must be
implemented by subclasses.  This might seem silly, since your program
will halt and catch fire when an unimplemented virtual method is hit
anyway, but there are some benefits.

%description -l pl
Class::Virtual jest podstawow± klas± do implementacji podstawowych
klas wirtualnych (przez niektórych nazywanych klasami abstrakcyjnymi).
Pozwala ona na jawne okre¶lenie, które metody s± wirtualne i musz±
byæ zaimplementowane w podklasach. Mo¿e siê to wydawaæ g³upie, gdy¿
program u¿ytkownika i tak stanie (i wznieci ogieñ) po natraieniu na
niezaimplementowan± metodê wirtualn±, ale rozwi±zanie to ma pewne
zalety.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/Virtual.pm
%{perl_vendorlib}/Class/Virtually
%{_mandir}/man3/*
