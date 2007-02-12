Summary:	Flare - a free ActionScript decompiler
Summary(pl.UTF-8):   Flare - darmowy dekompilator ActionScriptu
Name:		flare
Version:	0.60
Release:	1
License:	freeware
Group:		Development
Source0:	http://www.nowrap.de/download/%{name}06linux.tgz
# Source0-md5:	8a0779015bbb7fd26fbdc375ba14ac50
Source1:	%{name}.sh
URL:		http://www.nowrap.de/flare.html
Requires:	mktemp
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flare processes an SWF and extracts all scripts from it. The output is
written to a single text file. Only ActionScript is extracted, no text
or images.

%description -l pl.UTF-8
Flare przetwarza pliki SWF i wyciąga z niego wszystkie skrypty. Wynik
zapisywany jest do pojedynczego pliku tekstowego. Wyciągany jest tylko
ActionScript, żadnego tekstu ani obrazków.

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
