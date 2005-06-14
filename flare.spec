Summary:	Flare - a free ActionScript decompiler
Summary(pl):	Flare - darmowy dekompilator ActionScriptu
Name:		flare
Version:	0.51
Release:	0.1
License:	freeware
Group:		Development
Source0:	http://www.nowrap.de/download/%{name}05linux.tgz
# Source0-md5:	1267acb1857015145e80da14bd71d1b2
Source1:	%{name}.sh
URL:		http://www.nowrap.de/flare.html
Requires:	mktemp
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flare processes an SWF and extracts all scripts from it. The output is
written to a single text file. Only ActionScript is extracted, no text
or images.

%description -l pl
Flare przetwarza pliki SWF i wyci±ga z niego wszystkie skrypty. Wynik
zapisywany jest do pojedynczego pliku tekstowego. Wyci±gany jest tylko
ActionScript, ¿adnego tekstu ani obrazków.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install flare $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.TXT flare.html classic.css
%attr(755,root,root) %{_bindir}/flare
%attr(755,root,root) %{_bindir}/flare.sh
