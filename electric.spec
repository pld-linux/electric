Summary:	Electric VLSI Design System
Summary(pl):	System projektowania uk�ad�w VLSI
Name:		electric
Version:	6.01
Release:	1
License:	GPL
Vendor:		Static Free Software
Group:		Applications/Engineering
Group(de):	Applikationen/Ingenieurwesen
Group(pl):	Aplikacje/In�ynierskie
Source0:	ftp://ftp.gnu.org/pub/electric/%{name}-%{version}.tar.gz
Patch0:		%{name}-datadir.patch
BuildRequires:	lesstif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix	/usr/X11R6

%description
Electric designs MOS and bipolar integrated circuits,
printed-circuit-boards, or any type of circuit you choose. It has many
editing styles including layout, schematics, artwork, and
architectural specifications.

A large set of tools is available including design-rule checkers,
simulators, routers, layout generators, and more. Electric interfaces
to most popular CAD specifications including VHDL, CIF, and GDS II.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make} DEBUG="%{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/electric} 
install electric $RPM_BUILD_ROOT/%{_bindir}
install lib/.cadrc $RPM_BUILD_ROOT/%{_datadir}/electric
install lib/*.help $RPM_BUILD_ROOT/%{_datadir}/electric
install lib/*.mac $RPM_BUILD_ROOT/%{_datadir}/electric
install lib/*.txt $RPM_BUILD_ROOT/%{_datadir}/electric

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* ChangeLog*
%doc html/manual
%doc examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/electric
