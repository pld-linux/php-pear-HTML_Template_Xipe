%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Xipe
Summary:	%{_pearname} - A simple, fast and powerful template engine
Summary(pl.UTF-8):	%{_pearname} - prosty, szybki i potężny system szablonów
Name:		php-pear-%{_pearname}
Version:	1.7.6
Release:	5
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5b291d4e64e603f9e58ce0f517e3600
URL:		http://pear.php.net/package/HTML_Template_Xipe/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-Log >= 1.8
Requires:	php-pear-Tree >= 0.2
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

%description -l pl.UTF-8
Ten silnik szablonów to system kompilujący - wszystkie szablony są
kompilowane do plików PHP. Czyni to dostarczanie plików szybszym przy
kolejnych żądaniach, ponieważ szablony nie muszą być ponownie
kompilowane. Jeśli szablon zmieni się, musi być przekompilowany.

Nie trzeba się uczyć nowego języka szablonów. Poza trybem domyślnym,
są zestawy konstrukcji od wersji 1.6, pozwalające na edycję szablonów
edytorami WYSIWYG.

Domyślnie silnik używa wcięć do tworzenia bloków (można to wyłączyć).
Ta własność została zainspirowana Pythonem i potrzebą autora zmuszenia
się do pisania właściwego kodu HTML, przy użyciu właściwych wcięć, aby
uczynić kod bardziej czytelnym.

Każdy szablon można dostosować na wiele sposobów. Można konfigurować
każdy szablon lub cały katalog, aby używały różnych ograniczników,
parametrów buforowania itp. - poprzez plik XML lub fragment XML
osadzony gdziekolwiek wewnątrz kodu tpl.

Ostateczny plik (wynikowy plik HTML) także może być buforowany. Opcje
buforowania mogą być w miarę potrzeby modyfikowane. Buforowanie może
znacznie ograniczyć obciążenie serwera, bo nie musi być ponownie
przetwarzany cały plik PHP - czytelne dla klienta dane wynikowe są po
prostu dostarczane z bufora (dane są zapisywane przy użyciu mechanizmu
buforowania wyjścia w PHP).

Ten silnik jest przygotowany na używanie także w aplikacjach
wielojęzycznych. W przypadku używania PEAR::I18N do tłumaczenia
szablonu, skompilowane szablony muszą być zapisywane pod różną nazwą
dla każdego języka. Silnik także jest na to przygotowany - w razie
potrzeby zapisuje skompilowany szablon z użyciem kodu język (np.
skompilowany index.tpl zapisany dla języka angielskiego otrzymuje
nazwę index.tpl.en.php).

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
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
