%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Xipe
Summary:	%{_pearname} - A simple, fast and powerful template engine
Summary(pl):	%{_pearname} - prosty, szybki i potê¿ny system szablonów
Name:		php-pear-%{_pearname}
Version:	1.7.6
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5b291d4e64e603f9e58ce0f517e3600
URL:		http://pear.php.net/package/HTML_Template_Xipe/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Tree >= 0.2
Requires:	php-pear-Log >= 1.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The template engine is a compiling engine, all templates are compiled
into PHP-files. This will make the delivery of the files faster on the
next request, since the template doesn't need to be compiled again. If
the template changes it will be recompiled.

There is no new template language to learn. Beside the default mode,
there is a set of constructs since version 1.6 which allow you to edit
your templates with WYSIWYG editors.

By default the template engine uses indention for building blocks (you
can turn that off). This feature was inspired by Python and by the
need I felt to force myself to write proper HTML-code, using proper
indentions, to make the code better readable.

Every template is customizable in multiple ways. You can configure
each template or an entire directory to use different delimiters,
caching parameters, etc. via either an XML-file or a XML-chunk which
you simply write anywhere inside the tpl-code.

Using the Cache the final file can also be cached (i.e. a resulting
HTML-file). The caching options can be customized as needed. The cache
can reduce the server load by very much, since the entire php-file
doesn't need to be processed again, the resulting client-readable data
are simply delivered right from the cache (the data are saved using
php's output buffering).

The template engine is prepared to be used for multi-language
applications too. If you i.e. use the PEAR::I18N for translating the
template, the compiled templates need to be saved under a different
name for each language. The template engine is prepared for that too,
it saves the compiled template including the language code if required
(i.e. a compiled index.tpl which is saved for english gets the
filename index.tpl.en.php).

In PEAR status of this package is: %{_status}.

%description -l pl
Ten silnik szablonów to system kompiluj±cy - wszystkie szablony s±
kompilowane do plików PHP. Czyni to dostarczanie plików szybszym przy
kolejnych ¿±daniach, poniewa¿ szablony nie musz± byæ ponownie
kompilowane. Je¶li szablon zmieni siê, musi byæ przekompilowany.

Nie trzeba siê uczyæ nowego jêzyka szablonów. Poza trybem domy¶lnym,
s± zestawy konstrukcji od wersji 1.6, pozwalaj±ce na edycjê szablonów
edytorami WYSIWYG.

Domy¶lnie silnik u¿ywa wciêæ do tworzenia bloków (mo¿na to wy³±czyæ).
Ta w³asno¶æ zosta³a zainspirowana Pythonem i potrzeb± autora zmuszenia
siê do pisania w³a¶ciwego kodu HTML, przy u¿yciu w³a¶ciwych wciêæ, aby
uczyniæ kod bardziej czytelnym.

Ka¿dy szablon mo¿na dostosowaæ na wiele sposobów. Mo¿na konfigurowaæ
ka¿dy szablon lub ca³y katalog, aby u¿ywa³y ró¿nych ograniczników,
parametrów buforowania itp. - poprzez plik XML lub fragment XML
osadzony gdziekolwiek wewn±trz kodu tpl.

Ostateczny plik (wynikowy plik HTML) tak¿e mo¿e byæ buforowany. Opcje
buforowania mog± byæ w miarê potrzeby modyfikowane. Buforowanie mo¿e
znacznie ograniczyæ obci±¿enie serwera, bo nie musi byæ ponownie
przetwarzany ca³y plik PHP - czytelne dla klienta dane wynikowe s± po
prostu dostarczane z bufora (dane s± zapisywane przy u¿yciu mechanizmu
buforowania wyj¶cia w PHP).

Ten silnik jest przygotowany na u¿ywanie tak¿e w aplikacjach
wielojêzycznych. W przypadku u¿ywania PEAR::I18N do t³umaczenia
szablonu, skompilowane szablony musz± byæ zapisywane pod ró¿n± nazw±
dla ka¿dego jêzyka. Silnik tak¿e jest na to przygotowany - w razie
potrzeby zapisuje skompilowany szablon z u¿yciem kodu jêzyk (np.
skompilowany index.tpl zapisany dla jêzyka angielskiego otrzymuje
nazwê index.tpl.en.php).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Xipe
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Xipe/Filter
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Xipe/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Xipe/Filter/*.php
