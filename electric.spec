Summary:	Electric VLSI Design System
Summary(pl):	System projektowania uk³adów VLSI
Name:		electric
Version:	6.01
Release:	3
License:	GPL v2
Vendor:		Static Free Software
Group:		Applications/Engineering
Source0:	ftp://ftp.gnu.org/pub/gnu/electric/%{name}-%{version}.tar.gz
Patch0:		%{name}-datadir.patch
Patch1:		%{name}-tcl.patch
URL:		http://www.staticfreesoft.com/electric.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	lesstif-devel
BuildRequires:	tcl-devel
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

%description -l pl
Electric s³u¿y do projektowania uk³adów MOS i bipolarnych, p³ytek
drukowanych oraz dowolnych innych rodzajów uk³adów. Ma wiele styli
edycji, w tym rozmieszczenia, schematyczny, specyfikacji architektury.

Dostêpny jest du¿y zestaw narzêdzi, w tym symulatory, generatory itp.
S± dostêpne interfejsy do wiêkszo¶ci popularnych formatów CAD, w tym
VHDL, CIF i GDS II.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
aclocal
autoconf
%configure

%{__make} DEBUG="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/electric}
install electric $RPM_BUILD_ROOT%{_bindir}
install lib/.cadrc $RPM_BUILD_ROOT%{_datadir}/electric
install lib/*.help $RPM_BUILD_ROOT%{_datadir}/electric
install lib/*.mac $RPM_BUILD_ROOT%{_datadir}/electric
install lib/*.txt $RPM_BUILD_ROOT%{_datadir}/electric

# can't find better way to make electric find tcl.init
ln -sf /usr/lib/tcl8.* $RPM_BUILD_ROOT%{_datadir}/electric/tcl

gzip -9nf ChangeLog README examples/samples.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz html/manual examples
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/electric
%{_datadir}/electric/*
