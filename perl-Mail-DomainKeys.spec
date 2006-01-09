#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	DomainKeys
Summary:	Mail::Alias - implementation of Yahoo's mail signature protocol
Summary(pl):	Mail::Alias - implementacja protoko³u sygnatur pocztowych Yahoo
Name:		perl-Mail-DomainKeys
Version:	0.80
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e3da32a3bfa06b56d151093a194f2904
Patch0:		%{name}-notconnected.patch
BuildRequires:	perl-Crypt-OpenSSL-RSA
#BuildRequires:	perl-Mail-Address
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Net-DNS >= 0.34
#BuildRequires:	perl-Test-More
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::DomainKeys is a perl implementation of Yahoo's mail signature
protocol.

This library allows one to sign and verify signatures as per per draft
03 of the DomainKeys specification:

http://www.ietf.org/internet-drafts/draft-delany-domainkeys-base-03.txt

%description -l pl
Mail::DomainKeys jest implementacj± protoko³u sygnatur pocztowych Yahoo.

Ta biblioteka umo¿liwia sygnowanie i weryfikacje sygnatur zgodnie z
draftem 03 specyfikacji DomainKeys:

http://www.ietf.org/internet-drafts/draft-delany-domainkeys-base-03.txt

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp t/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{perl_vendorlib}/Mail/DomainKeys
%dir %{perl_vendorlib}/Mail/DomainKeys/Key
%{perl_vendorlib}/Mail/DomainKeys.pm
%{perl_vendorlib}/Mail/DomainKeys/*.pm
%{perl_vendorlib}/Mail/DomainKeys/Key/*.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
