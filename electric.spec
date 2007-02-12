Summary:	Electric VLSI Design System
Summary(pl.UTF-8):	System projektowania układów VLSI
Name:		electric
Version:	7.00
Release:	0.2
License:	GPL v2
Vendor:		Static Free Software
Group:		Applications/Engineering
Source0:	ftp://ftp.gnu.org/pub/gnu/electric/%{name}-%{version}.tar.gz
# Source0-md5:	64c89f820467b418d24ddf6c7e206c08
Source1:	%{name}.desktop
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-tcl.patch
Patch2:		%{name}-makefile.patch
Patch3:		%{name}-ac_fix.patch
URL:		http://www.staticfreesoft.com/electric.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	motif-devel
BuildRequires:	tcl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Electric designs MOS and bipolar integrated circuits,
printed-circuit-boards, or any type of circuit you choose. It has many
editing styles including layout, schematics, artwork, and
architectural specifications.

A large set of tools is available including design-rule checkers,
simulators, routers, layout generators, and more. Electric interfaces
to most popular CAD specifications including VHDL, CIF, and GDS II.

%description -l pl.UTF-8
Electric służy do projektowania układów MOS i bipolarnych, płytek
drukowanych oraz dowolnych innych rodzajów układów. Ma wiele styli
edycji, w tym rozmieszczenia, schematyczny, specyfikacji architektury.

Dostępny jest duży zestaw narzędzi, w tym symulatory, generatory itp.
Są dostępne interfejsy do większości popularnych formatów CAD, w tym
VHDL, CIF i GDS II.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2
%patch3

%build
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/electric,%{_desktopdir}}

install electric $RPM_BUILD_ROOT%{_bindir}
install lib/.cadrc $RPM_BUILD_ROOT%{_datadir}/electric
install lib/*.help $RPM_BUILD_ROOT%{_datadir}/electric
install lib/*.mac $RPM_BUILD_ROOT%{_datadir}/electric
install lib/*.txt $RPM_BUILD_ROOT%{_datadir}/electric

# can't find better way to make electric find tcl.init
ln -sf /usr/lib/tcl8.* $RPM_BUILD_ROOT%{_datadir}/electric/tcl

install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README examples/samples.txt html/manual examples
%attr(755,root,root) %{_bindir}/*
%{_datadir}/electric
%{_desktopdir}/*.desktop
