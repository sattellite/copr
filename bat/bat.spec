Name: bat
Version: 0.12.1
Release: 1%{?dist}
Summary: A cat(1) clone with wings.
License: MIT or Apache License, Version 2.0
URL: https://github.com/sharkdp/bat
Source0: https://github.com/sharkdp/bat/archive/v%{version}/bat-v%{version}.tar.gz
BuildRequires: cargo
%if 0%{?fedora} >= 24
ExclusiveArch: x86_64 i686 armv7hl
%else
ExclusiveArch: x86_64 aarch64
%endif

Patch0: https://raw.githubusercontent.com/sattellite/copr/master/bat/fix-build-0.12.patch

%description
A cat(1) clone with syntax highlighting, git integration and automatic paging.

# Disable debug info; bat doesn't include debug info in release profile
%define debug_package %{nil}
%prep
%autosetup -p1

%build
cargo build --release

%install
install -D -p -m 755 target/release/bat %{buildroot}%{_bindir}/bat
install -D -p -m 644 doc/bat.1 %{buildroot}%{_mandir}/man1/bat.1

%check
cargo test

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/bat
%{_mandir}/man1/bat.1*

%changelog
* Mon Sep 16 2019 Alexander Groshev <sattellite@yandex.com> - 0.12.1-1
- Update to 0.12.1 version

* Fri Feb 15 2019 Alexander Groshev <sattellite@yandex.com> - 0.10.0-1
- Update to 0.10.0 version

* Mon Nov 12 2018 Alexander Groshev <sattellite@yandex.com> - 0.9.0-1
- Update to 0.9.0 version

* Wed Nov 07 2018 Alexander Groshev <sattellite@yandex.com> - 0.8.0-1
- Initial spec file
