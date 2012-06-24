%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Template
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}_Xipe
Summary:	%{_pearname} - A simple, fast and powerful template engine
Summary(pl):	%{_pearname} - prosty, szybki i pot�ny system szablon�w
Name:		php-pear-%{_pearname}
Version:	1.7.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ee53750d19d846a01272e630ab37760f
URL:		http://opensource.visionp.de/modules/project/%{_pearname}.php
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear())'

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

This class has in PEAR status: %{_status}.

%description -l pl
Ten silnik szablon�w to system kompiluj�cy - wszystkie szablony s�
kompilowane do plik�w PHP. Czyni to dostarczanie plik�w szybszym przy
kolejnych ��daniach, poniewa� szablony nie musz� by� ponownie
kompilowane. Je�li szablon zmieni si�, musi by� przekompilowany.

Nie trzeba si� uczy� nowego j�zyka szablon�w. Poza trybem domy�lnym,
s� zestawy konstrukcji od wersji 1.6, pozwalaj�ce na edycj� szablon�w
edytorami WYSIWYG.

Domy�lnie silnik u�ywa wci�� do tworzenia blok�w (mo�na to wy��czy�).
Ta w�asno�� zosta�a zainspirowana Pythonem i potrzeb� autora zmuszenia
si� do pisania w�a�ciwego kodu HTML, przy u�yciu w�a�ciwych wci��, aby
uczyni� kod bardziej czytelnym.

Ka�dy szablon mo�na dostosowa� na wiele sposob�w. Mo�na konfigurowa�
ka�dy szablon lub ca�y katalog, aby u�ywa�y r�nych ogranicznik�w,
parametr�w buforowania itp. - poprzez plik XML lub fragment XML
osadzony gdziekolwiek wewn�trz kodu tpl.

Ostateczny plik (wynikowy plik HTML) tak�e mo�e by� buforowany. Opcje
buforowania mog� by� w miar� potrzeby modyfikowane. Buforowanie mo�e
znacznie ograniczy� obci��enie serwera, bo nie musi by� ponownie
przetwarzany ca�y plik PHP - czytelne dla klienta dane wynikowe s� po
prostu dostarczane z bufora (dane s� zapisywane przy u�yciu mechanizmu
buforowania wyj�cia w PHP).

Ten silnik jest przygotowany na u�ywanie tak�e w aplikacjach
wieloj�zycznych. W przypadku u�ywania PEAR::I18N do t�umaczenia
szablonu, skompilowane szablony musz� by� zapisywane pod r�n� nazw�
dla ka�dego j�zyka. Silnik tak�e jest na to przygotowany - w razie
potrzeby zapisuje skompilowany szablon z u�yciem kodu j�zyk (np.
skompilowany index.tpl zapisany dla j�zyka angielskiego otrzymuje
nazw� index.tpl.en.php).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Xipe/Filter

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/Xipe/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Xipe
install %{_pearname}-%{version}/Xipe/Filter/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Xipe/Filter

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Xipe
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Xipe/Filter
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Xipe/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Xipe/Filter/*.php
