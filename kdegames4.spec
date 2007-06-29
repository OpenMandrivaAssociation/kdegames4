%define _requires_exceptions devel\(libdns_sd\(.*\)\\|devel\(libdns_sd\)

%define revision 681524

%define use_enable_final 0
%{?_no_enable_final: %{expand: %%global use_enable_final 0}}

%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%define use_enable_pie 1
%{?_no_enable_pie: %{expand: %%global use_enable_pie 0}}

%if %unstable
%define dont_strip 1
%endif


# change compress method to bzip2
%define _source_payload w9.bzdio


%define lib_major 1
%define lib_name_orig libkdegames4
%define lib_name %mklibname kdegames4 %{lib_major}


Name:		kdegames4
Summary:	KDE - Games
Version:	3.91
Release: 	%mkrel 0.%revision.1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
Packager:	Mandriva Linux KDE Team <kde@mandriva.com>

URL:		ftp://ftp.kde.org/pub/kde/stable/%version/src/

%if %branch
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version.%revision.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdegames-%version.tar.bz2
%endif
Patch2:		kdegames-3.5.0-add-support-avahi.patch
BuildRoot:	%_tmppath/%name-%version-%release-root

BuildRequires: kdelibs4-devel
BuildRequires: libxml2-utils

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
	- katomic: build complex atoms with a minimal amount of moves
	- kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)
	- kbattleship: battleship game with built-in game server
	- kblackbox: find atoms in a grid by shooting electrons
	- kbounce: claim areas and don't get disturbed
	- klines: place 5 equal pieces together, but wait, there are 3 new ones
	- mahjongg: a tile laying patience
	- kmines: the classical mine sweeper
	- kolf: a golf game
	- konquest: conquer the planets of your enemy
	- kpat: several patience card games
	- kreversi: the old reversi board game, also known as othello
	- ksame: collect pieces of the same color
	- kshisen: patience game where you take away all pieces
	- ksirtet: very known if spelt this backwards
	- kspaceduel: two player game with shooting spaceships flying around a sun
	- ktuberling: kids game: make your own potato (NO french fries!)
	- kwin4: place 4 pieces in a row
	- libkdegames: KDE game library used by many of these programs
	- lskat: lieutnant skat

%files
%defattr(-,root,root)
%_kde_appsdir/kdegames/pics/star.png

#--------------------------------------------------------------------

%package -n %lib_name-devel
Summary:	Headers files for kdegames
Group:		Development/KDE and Qt

Provides:   %name-devel = %epoch:%version-%release
Provides:   %lib_name_orig-devel = %epoch:%version-%release
%define mini_release %mkrel 0.%revision.1
Requires:	kdelibs4-devel >= %version-%mini_release

%description -n %lib_name-devel
Headers files needed to build applications based on kdegames applications.

%files -n %lib_name-devel
%defattr(-,root,root,-)
%_kde_datadir/apps/cmake/modules/FindLibKDEGames.cmake
%_kde_datadir/apps/cmake/modules/GGZ.cmake
%_kde_datadir/apps/cmake/modules/FindLibKSirtet.cmake

%_kde_libdir/libkmahjongglib.so
%_kde_libdir/libkolflib.so
%_kde_libdir/libksirtetlib.so

%_kde_includedir/*.h

%dir %_kde_includedir/kgame/
%_kde_includedir/kgame/*.h

%dir %_kde_includedir/libksirtet/base/
%_kde_includedir/libksirtet/base/*.h
%dir %_kde_includedir/libksirtet/common/
%_kde_includedir/libksirtet/common/*.h
%dir %_kde_includedir/libksirtet/lib/
%_kde_includedir/libksirtet/lib/*.h
%dir %_kde_includedir/libksirtet/
%_kde_includedir/libksirtet/libksirtet_export.h

%_kde_includedir/KDE/KCardDialog
%_kde_includedir/KDE/KChat
%_kde_includedir/KDE/KChatBase
%_kde_includedir/KDE/KChatDialog
%_kde_includedir/KDE/KExtHighscore
%_kde_includedir/KDE/KGame/*
%_kde_includedir/KDE/KGameCanvas
%_kde_includedir/KDE/KGameLCD
%_kde_includedir/KDE/KGameMisc
%_kde_includedir/KDE/KGameProgress
%_kde_includedir/KDE/KGameSvgDigits
%_kde_includedir/KDE/KGameSvgDocument
%_kde_includedir/KDE/KGrid2D
%_kde_includedir/KDE/KHighscore
%_kde_includedir/KDE/KScoreDialog
%_kde_includedir/KDE/KStandardGameAction
%_kde_includedir/KDE/KGamePopupItem
%_kde_includedir/KDE/KGameTheme

%dir %_kde_includedir/highscore
%_kde_includedir/highscore/*.h

%dir %_kde_includedir/digits/
%_kde_includedir/digits/kgamesvgdigits.h

%_kde_libdir/libkdegames.so

%dir %_kde_datadir/config.kcfg/
%_kde_datadir/config.kcfg/*.kcfg


#-----------------------------------------------------------------------------

%package -n     kde4-kgoldrunner
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kgoldrunner4

%description -n kde4-kgoldrunner
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kgoldrunner
%defattr(-,root,root)
%attr(0755,root,root) %_kde_bindir/kgoldrunner
%_kde_datadir/applications/kde4/KGoldrunner.desktop
%dir %_kde_appsdir/kgoldrunner
%_kde_appsdir/kgoldrunner/kgoldrunnerui.rc
%_kde_appsdir/kgoldrunner/system
%_kde_appsdir/kgoldrunner/pics/*
%dir %_kde_docdir/HTML/en/kgoldrunner
%doc %_kde_docdir/HTML/en/kgoldrunner/index.cache.bz2
%doc %_kde_docdir/HTML/en/kgoldrunner/index.docbook
%doc %_kde_docdir/HTML/en/kgoldrunner/*.png
%_kde_iconsdir/hicolor/*/apps/kgoldrunner.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbackgammon
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kbackgammon4

%description -n kde4-kbackgammon
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kbackgammon
%defattr(-,root,root)
%_kde_bindir/kbackgammon
%_kde_datadir/applications/kde4/kbackgammon.desktop
%_kde_docdir/HTML/en/kbackgammon/board.png
%_kde_docdir/HTML/en/kbackgammon/index.cache.bz2
%_kde_docdir/HTML/en/kbackgammon/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/kbackgammon.png
%_kde_iconsdir/hicolor/16x16/apps/kbackgammon.png
%_kde_iconsdir/hicolor/16x16/apps/kbackgammon_engine.png
%_kde_iconsdir/hicolor/22x22/apps/kbackgammon.png
%_kde_iconsdir/hicolor/32x32/apps/kbackgammon.png
%_kde_iconsdir/hicolor/32x32/apps/kbackgammon_engine.png
%_kde_iconsdir/hicolor/48x48/apps/kbackgammon.png
%_kde_iconsdir/hicolor/48x48/apps/kbackgammon_engine.png
%_kde_iconsdir/hicolor/64x64/apps/kbackgammon.png
%_kde_iconsdir/hicolor/64x64/apps/kbackgammon_engine.png
%_kde_appsdir/kbackgammon/kbackgammonui.rc
%_kde_appsdir/kbackgammon/pics/*
%dir %_kde_appsdir/kbackgammon/sounds
%_kde_appsdir/kbackgammon/sounds/*
%_kde_appsdir/kbackgammon/kbackgammon.notifyrc

#-----------------------------------------------------------------------------

%package -n     kde4-katomic
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       katomic4

%description -n kde4-katomic
katomic: build complex atoms with a minimal amount of moves

%files -n kde4-katomic
%defattr(-,root,root)
%_kde_bindir/katomic
%_kde_datadir/applications/kde4/katomic.desktop
%doc %_kde_docdir/HTML/en/katomic/index.cache.bz2
%doc%_kde_docdir/HTML/en/katomic/index.docbook
%_kde_iconsdir/hicolor/*/apps/katomic.png
%_kde_appsdir/katomic/levels/*
%_kde_appsdir/katomic/pics/default_theme.svgz
%_kde_appsdir/katomic/katomicui.rc

#-----------------------------------------------------------------------------

%package -n     kde4-kblackbox
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kblackbox4

%description -n kde4-kblackbox
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kblackbox
%defattr(-,root,root)
%_kde_bindir/kblackbox
%_kde_datadir/applications/kde4/kblackbox.desktop
%_kde_appsdir/kblackbox/kblackboxui.rc
%_kde_appsdir/kblackbox/pics/kblackbox.svgz
%_kde_docdir/HTML/en/kblackbox/index.cache.bz2
%_kde_docdir/HTML/en/kblackbox/index.docbook
%_kde_docdir/HTML/en/kblackbox/kblackboxtbar.png
%_kde_iconsdir/hicolor/128x128/apps/kblackbox.png
%_kde_iconsdir/hicolor/16x16/apps/kblackbox.png
%_kde_iconsdir/hicolor/22x22/apps/kblackbox.png
%_kde_iconsdir/hicolor/32x32/apps/kblackbox.png
%_kde_iconsdir/hicolor/48x48/apps/kblackbox.png
%_kde_iconsdir/hicolor/64x64/apps/kblackbox.png

#-----------------------------------------------------------------------------

%package -n     kde4-ktuberling
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ktuberling4

%description -n kde4-ktuberling
Headers files needed to build applications based on kdegames applications.


%files -n kde4-ktuberling
%defattr(-,root,root)
%_kde_bindir/ktuberling
%_kde_datadir/applications/kde4/ktuberling.desktop
%_kde_appsdir/ktuberling/ktuberlingui.rc
%_kde_appsdir/ktuberling/sounds
%_kde_appsdir/ktuberling/sounds/en
%_kde_appsdir/ktuberling/sounds/en/*.wav
%_kde_appsdir/ktuberling/pics/default_theme.svg
%_kde_appsdir/ktuberling/pics/default_theme.theme
%_kde_appsdir/ktuberling/pics/potato-game.svg
%_kde_appsdir/ktuberling/pics/potato-game.theme
%dir %_kde_docdir/HTML/en/ktuberling
%_kde_docdir/HTML/en/ktuberling/*.png
%_kde_docdir/HTML/en/ktuberling/index.cache.bz2
%_kde_docdir/HTML/en/ktuberling/index.docbook
%_kde_docdir/HTML/en/ktuberling/technical-reference.docbook
%_kde_iconsdir/hicolor/*/apps/ktuberling.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbounce
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kbounce4

%description -n kde4-kbounce
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kbounce
%defattr(-,root,root)
%_kde_bindir/kbounce
%_kde_datadir/applications/kde4/kbounce.desktop
%_kde_appsdir/kbounce/kbounceui.rc
%_kde_appsdir/kbounce/themes/*
%dir %_kde_datadir/apps/kbounce/sounds
%_kde_datadir/apps/kbounce/sounds/*.au
%_kde_docdir/HTML/en/kbounce/index.cache.bz2
%_kde_docdir/HTML/en/kbounce/index.docbook
%_kde_docdir/HTML/en/kbounce/jezball_corridor1.png
%_kde_docdir/HTML/en/kbounce/jezball_corridor2.png
%_kde_docdir/HTML/en/kbounce/jezball_newWall.png

#-----------------------------------------------------------------------------

%package -n     kde4-kspaceduel
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kspaceduel4

%description -n kde4-kspaceduel
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kspaceduel
%defattr(-,root,root)
%_kde_bindir/kspaceduel
%_kde_appsdir/kspaceduel/icons
%_kde_appsdir/kspaceduel/icons/locolor
%_kde_appsdir/kspaceduel/icons/locolor/16x16
%_kde_appsdir/kspaceduel/icons/locolor/16x16/actions
%_kde_appsdir/kspaceduel/icons/locolor/16x16/actions/spnewgame.png
%_kde_appsdir/kspaceduel/icons/locolor/16x16/actions/spnewround.png
%_kde_appsdir/kspaceduel/icons/locolor/16x16/actions/sppausegame.png
%_kde_appsdir/kspaceduel/sprites/playerinfo/*.png
%_kde_appsdir/kspaceduel/sprites/backgr.png
%_kde_appsdir/kspaceduel/sprites/default_theme.svgz
%_kde_appsdir/kspaceduel/kspaceduelui.rc
%_kde_datadir/config.kcfg/kspaceduel.kcfg
%_kde_docdir/HTML/en/kspaceduel/index.cache.bz2
%_kde_docdir/HTML/en/kspaceduel/index.docbook
%_kde_docdir/HTML/en/kspaceduel/kspaceduel3.png
%_kde_iconsdir/hicolor/*/apps/kspaceduel.png

#-----------------------------------------------------------------------------

%package -n     kde4-kreversi
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kreversi4

%description -n kde4-kreversi
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kreversi
%defattr(-,root,root)
%_kde_bindir/kreversi
%_kde_datadir/applications/kde4/kreversi.desktop
%_kde_appsdir/kreversi/sounds
%_kde_appsdir/kreversi/sounds/reversi-click.wav
%_kde_appsdir/kreversi/sounds/reversi-won.wav
%_kde_appsdir/kreversi/pics/*
%_kde_appsdir/kreversi/kreversi.notifyrc
%_kde_appsdir/kreversi/kreversiui.rc
%_kde_iconsdir/hicolor/*/apps/kreversi.png
%dir %_kde_docdir/HTML/en/kreversi
%doc %_kde_docdir/HTML/en/kreversi/index.cache.bz2
%doc %_kde_docdir/HTML/en/kreversi/index.docbook
%doc %_kde_docdir/HTML/en/kreversi/kreversi-configuration.png
%doc %_kde_docdir/HTML/en/kreversi/kreversi1.png

#-----------------------------------------------------------------------------

%package -n     kde4-kolf
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kolf4

%description -n kde4-kolf
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kolf
%defattr(-,root,root)
%_kde_bindir/kolf
%_kde_datadir/applications/kde4/kolf.desktop
%_kde_appsdir/kolf/courses
%_kde_appsdir/kolf/courses/Classic.kolf
%_kde_appsdir/kolf/courses/Easy.kolf
%_kde_appsdir/kolf/courses/Hard.kolf
%_kde_appsdir/kolf/courses/Impossible
%_kde_appsdir/kolf/courses/Medium.kolf
%_kde_appsdir/kolf/courses/Practice
%_kde_appsdir/kolf/courses/ReallyEasy
%_kde_appsdir/kolf/courses/USApro
%_kde_appsdir/kolf/intro
%_kde_appsdir/kolf/kolfui.rc
%_kde_appsdir/kolf/pics
%_kde_appsdir/kolf/pics/cup.png
%_kde_appsdir/kolf/pics/grass.png
%_kde_appsdir/kolf/pics/puddle.png
%_kde_appsdir/kolf/pics/sand.png
%_kde_appsdir/kolf/sounds
%_kde_appsdir/kolf/sounds/blackhole.wav
%_kde_appsdir/kolf/sounds/blackholeeject.wav
%_kde_appsdir/kolf/sounds/blackholeputin.wav
%_kde_appsdir/kolf/sounds/hit.wav
%_kde_appsdir/kolf/sounds/holed.wav
%_kde_appsdir/kolf/sounds/holeinone.wav
%_kde_appsdir/kolf/sounds/puddle.wav
%_kde_appsdir/kolf/sounds/wall.wav
%_kde_appsdir/kolf/tutorial.kolf
%_kde_appsdir/kolf/tutorial.kolfgame
%_kde_docdir/HTML/en/kolf/index.cache.bz2
%_kde_docdir/HTML/en/kolf/index.docbook
%_kde_datadir/icons/hicolor/*/apps/kolf.png

#-----------------------------------------------------------------------------

%package -n     kde4-konquest
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       konquest4

%description -n kde4-konquest
Headers files needed to build applications based on kdegames applications.


%files -n kde4-konquest
%defattr(-,root,root)
%_kde_bindir/konquest
%_kde_datadir/applications/kde4/konquest.desktop
%_kde_appsdir/konquest/konquestui.rc
%_kde_appsdir/konquest/pics
%_kde_appsdir/konquest/pics/konquest-splash.png
%_kde_appsdir/konquest/pics/planet1.xpm
%_kde_appsdir/konquest/pics/planet2.xpm
%_kde_appsdir/konquest/pics/planet3.xpm
%_kde_appsdir/konquest/pics/planet4.xpm
%_kde_appsdir/konquest/pics/planet5.xpm
%_kde_appsdir/konquest/pics/planet6.xpm
%_kde_appsdir/konquest/pics/planet7.xpm
%_kde_appsdir/konquest/pics/planet8.xpm
%_kde_appsdir/konquest/pics/planet9.xpm
%_kde_appsdir/konquest/pics/ruler.xpm
%_kde_docdir/HTML/en/konquest/index.cache.bz2
%_kde_docdir/HTML/en/konquest/index.docbook
%_kde_datadir/icons/hicolor/*/apps/konquest.png


#-----------------------------------------------------------------------------

%package -n     kde4-ksame
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksame4

%description -n kde4-ksame
Headers files needed to build applications based on kdegames applications.


%files -n kde4-ksame
%defattr(-,root,root)
%_kde_bindir/ksame
%_kde_appsdir/ksame/ksameui.rc
%dir %_kde_docdir/HTML/en/ksame
%doc %_kde_docdir/HTML/en/ksame/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksame/index.docbook
%_kde_datadir/icons/hicolor/*/apps/ksame.png

#-----------------------------------------------------------------------------

%package -n     kde4-kmahjongg
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kmahjongg4

%description -n kde4-kmahjongg
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kmahjongg
%defattr(-,root,root)
%_kde_bindir/kmahjongg
%_kde_datadir/applications/kde4/kmahjongg.desktop
%_kde_appsdir/kmahjongg/kmahjonggui.rc
%_kde_appsdir/kmahjongg/pics/*
%_kde_appsdir/kmahjongglib/backgrounds/*
%_kde_appsdir/kmahjongglib/tilesets/*
%_kde_datadir/config.kcfg/kmahjongg.kcfg
%dir %_kde_docdir/HTML/en/kmahjongg
%doc %_kde_docdir/HTML/en/kmahjongg/index.cache.bz2
%doc %_kde_docdir/HTML/en/kmahjongg/index.docbook
%doc %_kde_docdir/HTML/en/kmahjongg/*.png
%_kde_datadir/icons/hicolor/*/apps/kmahjongg.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbattleship
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kbattleship4

%description -n kde4-kbattleship
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kbattleship
%defattr(-,root,root)
%_kde_bindir/kbattleship
%_kde_datadir/applications/kde4/kbattleship.desktop
%_kde_docdir/HTML/en/kbattleship/index.cache.bz2
%_kde_docdir/HTML/en/kbattleship/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/kbattleship.png
%_kde_iconsdir/hicolor/16x16/apps/kbattleship.png
%_kde_iconsdir/hicolor/22x22/apps/kbattleship.png
%_kde_iconsdir/hicolor/32x32/apps/kbattleship.png
%_kde_iconsdir/hicolor/48x48/apps/kbattleship.png
%_kde_iconsdir/hicolor/64x64/apps/kbattleship.png
%_kde_appsdir/kbattleship/kbattleshipui.rc
%_kde_appsdir/kbattleship/pictures/default_theme.svgz
%_kde_appsdir/kbattleship/sounds/*

#-----------------------------------------------------------------------------

%package -n     kde4-kiriki
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kiriki4

%description -n kde4-kiriki
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kiriki
%defattr(-,root,root)
%_kde_bindir/kiriki
%_kde_datadir/applications/kde4/kiriki.desktop
%_kde_docdir/HTML/en/kiriki/index.cache.bz2
%_kde_docdir/HTML/en/kiriki/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/kiriki.png
%_kde_iconsdir/hicolor/16x16/apps/kiriki.png
%_kde_iconsdir/hicolor/22x22/apps/kiriki.png
%_kde_iconsdir/hicolor/32x32/apps/kiriki.png
%_kde_iconsdir/hicolor/48x48/apps/kiriki.png
%_kde_iconsdir/hicolor/64x64/apps/kiriki.png
%_kde_appsdir/kiriki/images/*
%_kde_appsdir/kiriki/kirikiui.rc

#-----------------------------------------------------------------------------

%package -n     kde4-ksudoku
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksudoku4

%description -n kde4-ksudoku
Headers files needed to build applications based on kdegames applications.


%files -n kde4-ksudoku
%defattr(-,root,root)
%_kde_bindir/ksudoku
%_kde_datadir/applications/kde4/ksudoku.desktop
%_kde_appsdir/ksudoku/4x4.desktop
%_kde_appsdir/ksudoku/4x4.xml
%_kde_appsdir/ksudoku/Jigsaw.desktop
%_kde_appsdir/ksudoku/Jigsaw.xml
%_kde_appsdir/ksudoku/Samurai.desktop
%_kde_appsdir/ksudoku/Samurai.xml
%_kde_appsdir/ksudoku/XSudoku.desktop
%_kde_appsdir/ksudoku/XSudoku.xml
%_kde_appsdir/ksudoku/ksudokuui.rc
%_kde_datadir/config/ksudokurc
%_kde_docdir/HTML/en/ksudoku/index.cache.bz2
%_kde_docdir/HTML/en/ksudoku/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/ksudoku.png
%_kde_iconsdir/hicolor/16x16/apps/ksudoku.png
%_kde_iconsdir/hicolor/32x32/apps/ksudoku.png

#-----------------------------------------------------------------------------

%package -n     kde4-bovo
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       bovo4

%description -n kde4-bovo
Headers files needed to build applications based on kdegames applications.


%files -n kde4-bovo
%defattr(-,root,root)
%_kde_bindir/bovo
%_kde_datadir/applications/kde4/bovo.desktop
%_kde_appsdir/bovo/bovoui.rc
%_kde_appsdir/bovo/themes/gomoku/theme.svg
%_kde_appsdir/bovo/themes/gomoku/themerc
%_kde_appsdir/bovo/themes/highcontrast/theme.svg
%_kde_appsdir/bovo/themes/highcontrast/themerc
%_kde_appsdir/bovo/themes/scribble/theme.svg
%_kde_appsdir/bovo/themes/scribble/themerc
%_kde_appsdir/bovo/themes/spacy/theme.svg
%_kde_appsdir/bovo/themes/spacy/themerc
%_kde_docdir/HTML/en/bovo/index.cache.bz2
%_kde_docdir/HTML/en/bovo/index.docbook

#-----------------------------------------------------------------------------

%package -n     kde4-kjumpingcube
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kjumpingcube4

%description -n kde4-kjumpingcube
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kjumpingcube
%defattr(-,root,root)
%_kde_bindir/kjumpingcube
%_kde_datadir/applications/kde4/kjumpingcube.desktop
%_kde_appsdir/kjumpingcube/kjumpingcubeui.rc
%_kde_appsdir/kjumpingcube/pics/default.desktop
%_kde_appsdir/kjumpingcube/pics/default.svg
%_kde_docdir/HTML/en/kjumpingcube/index.cache.bz2
%_kde_docdir/HTML/en/kjumpingcube/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/kjumpingcube.png
%_kde_iconsdir/hicolor/16x16/apps/kjumpingcube.png
%_kde_iconsdir/hicolor/22x22/apps/kjumpingcube.png
%_kde_iconsdir/hicolor/32x32/apps/kjumpingcube.png
%_kde_iconsdir/hicolor/48x48/apps/kjumpingcube.png
%_kde_iconsdir/hicolor/64x64/apps/kjumpingcube.png

#-----------------------------------------------------------------------------

%package -n     kde4-klines
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       klines4

%description -n kde4-klines
Headers files needed to build applications based on kdegames applications.


%files -n kde4-klines
%defattr(-,root,root)
%_kde_bindir/klines
%_kde_datadir/applications/kde4/klines.desktop
%_kde_appsdir/klines/klinesui.rc
%_kde_appsdir/klines/themes/default.desktop
%_kde_appsdir/klines/themes/klines.svgz
%_kde_docdir/HTML/en/klines/index.cache.bz2
%_kde_docdir/HTML/en/klines/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/klines.png
%_kde_iconsdir/hicolor/16x16/apps/klines.png
%_kde_iconsdir/hicolor/22x22/apps/klines.png
%_kde_iconsdir/hicolor/32x32/apps/klines.png
%_kde_iconsdir/hicolor/48x48/apps/klines.png
%_kde_iconsdir/hicolor/64x64/apps/klines.png

#-----------------------------------------------------------------------------

%package -n     kde4-kmines
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kmines4

%description -n kde4-kmines
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kmines
%defattr(-,root,root)
%_kde_bindir/kmines
%_kde_datadir/applications/kde4/kmines.desktop
%_kde_appsdir/kmines/kmines.notifyrc
%_kde_appsdir/kmines/kminesui.rc
%_kde_appsdir/kmines/themes/classic.desktop
%_kde_appsdir/kmines/themes/classic_preview.png
%_kde_appsdir/kmines/themes/default.desktop
%_kde_appsdir/kmines/themes/default_preview.png
%_kde_appsdir/kmines/themes/kmines_classic.svgz
%_kde_appsdir/kmines/themes/kmines_oxygen.svgz
%_kde_datadir/config/kmines.knsrc
%_kde_docdir/HTML/en/kmines/index.cache.bz2
%_kde_docdir/HTML/en/kmines/index.docbook
%_kde_docdir/HTML/en/kmines/kmines1.png
%_kde_docdir/HTML/en/kmines/kmines2.png
%_kde_iconsdir/hicolor/128x128/apps/kmines.png
%_kde_iconsdir/hicolor/16x16/apps/kmines.png
%_kde_iconsdir/hicolor/22x22/apps/kmines.png
%_kde_iconsdir/hicolor/32x32/apps/kmines.png
%_kde_iconsdir/hicolor/48x48/apps/kmines.png
%_kde_iconsdir/hicolor/64x64/apps/kmines.png

#-----------------------------------------------------------------------------

%package -n     kde4-knetwalk
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       knetwalk4

%description -n kde4-knetwalk
Headers files needed to build applications based on kdegames applications.


%files -n kde4-knetwalk
%defattr(-,root,root)
%_kde_bindir/knetwalk
%_kde_datadir/applications/kde4/knetwalk.desktop
%_kde_appsdir/knetwalk/all.svgz
%_kde_appsdir/knetwalk/knetwalk.notifyrc
%_kde_appsdir/knetwalk/knetwalkui.rc
%_kde_appsdir/knetwalk/sounds/click.wav
%_kde_appsdir/knetwalk/sounds/connect.wav
%_kde_appsdir/knetwalk/sounds/start.wav
%_kde_appsdir/knetwalk/sounds/turn.wav
%_kde_appsdir/knetwalk/sounds/win.wav
%_kde_iconsdir/hicolor/128x128/apps/knetwalk.png
%_kde_iconsdir/hicolor/16x16/apps/knetwalk.png
%_kde_iconsdir/hicolor/22x22/apps/knetwalk.png
%_kde_iconsdir/hicolor/32x32/apps/knetwalk.png
%_kde_iconsdir/hicolor/48x48/apps/knetwalk.png
%_kde_iconsdir/hicolor/64x64/apps/knetwalk.png
%_kde_iconsdir/hicolor/scalable/apps/knetwalk.svgz

#-----------------------------------------------------------------------------

%package -n     kde4-kpat
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kpat4

%description -n kde4-kpat
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kpat
%defattr(-,root,root)
%_kde_bindir/kpat
%_kde_datadir/applications/kde4/kpat.desktop
%_kde_appsdir/kpat/backgrounds/background.svg
%_kde_appsdir/kpat/kpatui.rc
%_kde_appsdir/kpat/pile.svg
%_kde_appsdir/kpat/won.svg
%_kde_docdir/HTML/en/kpat/clubs.png
%_kde_docdir/HTML/en/kpat/diamonds.png
%_kde_docdir/HTML/en/kpat/hearts.png
%_kde_docdir/HTML/en/kpat/index.cache.bz2
%_kde_docdir/HTML/en/kpat/index.docbook
%_kde_docdir/HTML/en/kpat/man-kpat.6.docbook
%_kde_docdir/HTML/en/kpat/playfield.png
%_kde_docdir/HTML/en/kpat/spades.png
%_kde_iconsdir/hicolor/128x128/apps/kpat.png
%_kde_iconsdir/hicolor/16x16/apps/kpat.png
%_kde_iconsdir/hicolor/22x22/apps/kpat.png
%_kde_iconsdir/hicolor/32x32/apps/kpat.png
%_kde_iconsdir/hicolor/48x48/apps/kpat.png
%_kde_iconsdir/hicolor/64x64/apps/kpat.png

#-----------------------------------------------------------------------------

%package -n     kde4-kshisen
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kshisen4

%description -n kde4-kshisen
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kshisen
%defattr(-,root,root)
%_kde_bindir/kshisen
%_kde_datadir/applications/kde4/kshisen.desktop
%_kde_appsdir/kshisen/kshisenui.rc
%_kde_docdir/HTML/en/kshisen/index.cache.bz2
%_kde_docdir/HTML/en/kshisen/index.docbook
%_kde_docdir/HTML/en/kshisen/kshisen-configuration.png
%_kde_docdir/HTML/en/kshisen/score-formula.png
%_kde_iconsdir/hicolor/128x128/apps/kshisen.png
%_kde_iconsdir/hicolor/16x16/apps/kshisen.png
%_kde_iconsdir/hicolor/22x22/apps/kshisen.png
%_kde_iconsdir/hicolor/32x32/apps/kshisen.png
%_kde_iconsdir/hicolor/48x48/apps/kshisen.png
%_kde_iconsdir/hicolor/64x64/apps/kshisen.png

#-----------------------------------------------------------------------------

%package -n     kde4-ksquares
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksquares4

%description -n kde4-ksquares
Headers files needed to build applications based on kdegames applications.


%files -n kde4-ksquares
%defattr(-,root,root)
%_kde_bindir/ksquares
%_kde_datadir/applications/kde4/ksquares.desktop
%_kde_appsdir/ksquares/ksquaresui.rc
%_kde_docdir/HTML/en/ksquares/index.cache.bz2
%_kde_docdir/HTML/en/ksquares/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/ksquares.png
%_kde_iconsdir/hicolor/16x16/apps/ksquares.png
%_kde_iconsdir/hicolor/22x22/apps/ksquares.png
%_kde_iconsdir/hicolor/32x32/apps/ksquares.png
%_kde_iconsdir/hicolor/48x48/apps/ksquares.png
%_kde_iconsdir/hicolor/64x64/apps/ksquares.png
%_kde_iconsdir/hicolor/scalable/actions/ksquares_ai.svgz
%_kde_iconsdir/hicolor/scalable/actions/ksquares_display.svgz

#-----------------------------------------------------------------------------

%package -n     kde4-kwin4
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kwin44

%description -n kde4-kwin4
Headers files needed to build applications based on kdegames applications.


%files -n kde4-kwin4
%defattr(-,root,root)
%_kde_bindir/kwin4
%_kde_bindir/kwin4proc
%_kde_datadir/applications/kde4/kwin4.desktop
%_kde_appsdir/kwin4/grafix/default.rc
%_kde_appsdir/kwin4/grafix/default.svg
%_kde_appsdir/kwin4/grafix/index.desktop
%_kde_appsdir/kwin4/grafix/yellow.rc
%_kde_appsdir/kwin4/grafix/yellow.svg
%_kde_appsdir/kwin4/kwin4ui.rc
%_kde_docdir/HTML/en/kwin4/index.cache.bz2
%_kde_docdir/HTML/en/kwin4/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/kwin4.png
%_kde_iconsdir/hicolor/16x16/apps/kwin4.png
%_kde_iconsdir/hicolor/22x22/apps/kwin4.png
%_kde_iconsdir/hicolor/32x32/apps/kwin4.png
%_kde_iconsdir/hicolor/48x48/apps/kwin4.png
%_kde_iconsdir/hicolor/64x64/apps/kwin4.png

#-----------------------------------------------------------------------------

%package -n     kde4-lskat
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       lskat4

%description -n kde4-lskat
Headers files needed to build applications based on kdegames applications.


%files -n kde4-lskat
%defattr(-,root,root)
%_kde_bindir/lskat
%_kde_datadir/applications/kde4/lskat.desktop
%_kde_appsdir/lskat/grafix/default.rc
%_kde_appsdir/lskat/grafix/default.svg
%_kde_appsdir/lskat/lskatui.rc
%_kde_docdir/HTML/en/lskat/index.cache.bz2
%_kde_docdir/HTML/en/lskat/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/lskat.png
%_kde_iconsdir/hicolor/16x16/apps/lskat.png
%_kde_iconsdir/hicolor/22x22/apps/lskat.png
%_kde_iconsdir/hicolor/32x32/apps/lskat.png
%_kde_iconsdir/hicolor/48x48/apps/lskat.png
%_kde_iconsdir/hicolor/64x64/apps/lskat.png

#-----------------------------------------------------------------------------

%package -n     kde4-ksirtet
Summary:        Headers files for kdegames
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksirtet4

%description -n kde4-ksirtet
Headers files needed to build applications based on kdegames applications.


%files -n kde4-ksirtet
%defattr(-,root,root)
%_kde_datadir/applications/kde4/ksirtet.desktop
%_kde_appsdir/ksirtet/ksirtet.notifyrc
%_kde_appsdir/ksirtet/ksirtetui.rc
%_kde_docdir/HTML/en/ksirtet/index.cache.bz2
%_kde_docdir/HTML/en/ksirtet/index.docbook
%_kde_iconsdir/hicolor/128x128/apps/ksirtet.png
%_kde_iconsdir/hicolor/16x16/apps/ksirtet.png
%_kde_iconsdir/hicolor/22x22/apps/ksirtet.png
%_kde_iconsdir/hicolor/32x32/apps/ksirtet.png
%_kde_iconsdir/hicolor/48x48/apps/ksirtet.png
%_kde_iconsdir/hicolor/64x64/apps/ksirtet.png

#-----------------------------------------------------------------------------

%define libkdegames %mklibname kdegames 5

%package -n %libkdegames
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkdegames
KDE 4 library.

%post -n %libkdegames -p /sbin/ldconfig
%postun -n %libkdegames -p /sbin/ldconfig

%files -n %libkdegames
%defattr(-,root,root)
%_kde_libdir/libkdegames.so.*

#-----------------------------------------------------------------------------

%define libkmahjongglib %mklibname kmahjongglib 5

%package -n %libkmahjongglib
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkmahjongglib
KDE 4 library.

%post -n %libkmahjongglib -p /sbin/ldconfig
%postun -n %libkmahjongglib -p /sbin/ldconfig

%files -n %libkmahjongglib
%defattr(-,root,root)
%_kde_libdir/libkmahjongglib.so.*

#-----------------------------------------------------------------------------

%define libkolflib %mklibname kolflib 1.2.0

%package -n %libkolflib
Summary: KDE 4 library
Group: System/Libraries

%description -n %libkolflib
KDE 4 library.

%post -n %libkolflib -p /sbin/ldconfig
%postun -n %libkolflib -p /sbin/ldconfig

%files -n %libkolflib
%defattr(-,root,root)
%_kde_libdir/libkolflib.so.*

#-----------------------------------------------------------------------------

%define libksirtetlib %mklibname ksirtetlib 1.2.0

%package -n %libksirtetlib
Summary: KDE 4 library
Group: System/Libraries

%description -n %libksirtetlib
KDE 4 library.

%post -n %libksirtetlib -p /sbin/ldconfig
%postun -n %libksirtetlib -p /sbin/ldconfig

%files -n %libksirtetlib
%defattr(-,root,root)
%_kde_libdir/libksirtetlib.so.*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdegames

%build

cd $RPM_BUILD_DIR/kdegames

%cmake_kde4 \
%if %use_enable_final
      -DKDE4_ENABLE_FINAL=ON \
%endif
%if %use_enable_pie
      -DKDE4_ENABLE_FPIE=ON \
%endif
%if %unstable
      -DCMAKE_BUILD_TYPE=debug
%endif


%make


%install
rm -fr %buildroot

cd $RPM_BUILD_DIR/kdegames/build

# David - 2.2-0.alpha2.3mdk - Don't strip when we are not in final release
%if %unstable
export DONT_STRIP=1
%endif

make install DESTDIR=%buildroot 



install -d %buildroot/%_iconsdir/mini/
install -d %buildroot/%_iconsdir/large/

%post
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache crystalsvg
%update_icon_cache hicolor

%postun
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache crystalsvg
%clean_icon_cache hicolor

%post -n %lib_name-devel -p /sbin/ldconfig

%postun -n %lib_name-devel -p /sbin/ldconfig

%clean
rm -fr %buildroot

