Summary:	TTA Lossless Audio compressor
Summary(pl.UTF-8):	Bezstratny kompresor dźwięku TTA
Name:		ttaenc
Version:	3.4.1
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	https://downloads.sourceforge.net/tta/%{name}-%{version}-src.tgz
# Source0-md5:	c9ab8194984b34e7f7bf55d579c97f39
URL:		https://sourceforge.net/projects/tta/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
TTA performs lossless compression on multichannel 8, 16 and 24 bits
data of the Wav audio files. Being "lossless" means that no data-
quality is lost in the compression - when uncompressed, the data will
be identical to the original. The compression ratios of TTA depend on
the type of music file being compressed, but the compression size
will generally range between 30%% - 70%% of the original. TTA format
supports both of ID3v1/v2 and APEv2 tags. Detailed format description
is available at <http://tta.sourceforge.net/>.

%description -l pl.UTF-8
TTA kompresuje bezstratnie wielokanałowe, 8-, 16- i 24-bitowe dane
dźwiękowe z plików Wav. "Bezstratnie" oznacza, że żadna jakość danych
nie jest tracona - po dekompresji dane będą identyczne z oryginałem.
Współczynniki kompresji TTA zależą od rodzaju pliku muzycznego, ale
zwykle wynoszą od 30%% do 70%%. Format TTA obsługuje znaczniki
ID3v1/v2 oraz APEv2. Szczegóły formatu można znaleźć pod adresem
<http://tta.sourceforge.net/>.

%prep
%setup -q -n %{name}-%{version}-src

%{__sed} -i -e 's/__inline/static inline/' ttaenc.c

%build
%{__make} \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -D ttaenc $RPM_BUILD_ROOT%{_bindir}/ttaenc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog-3.4.1 README
%attr(755,root,root) %{_bindir}/ttaenc
