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
	- ksirtet: Ksirtet: clone of the well known Tetris game family
	- kspaceduel: two player game with shooting spaceships flying around a sun
	- ktuberling: kids game: make your own potato (NO french fries!)
	- kwin4: place 4 pieces in a row
	- Lskat: lieutnant skat
	- Ksudoku: Play, create and solve sudoku grids
	- KGoldrunner: a game of action and puzzle solving.
	- KTuberling: "potato editor" game
	- Kiriki: a dice game
	- Kjumpingcube: a tactical game for number-crunchers
	- Bovo: classic pen and paper game
	- KSquares: an implementation of the popular paper based game squares
	- Knetwalk: Turn the board pieces to get all computers connected²

%post
/sbin/ldconfig
%update_icon_cache oxygen

%postun
/sbin/ldconfig
%clean_icon_cache oxygen

%files
%defattr(-,root,root)
%_kde_appsdir/kdegames/pics/star.png
%_kde_appsdir/carddecks/*
%_kde_appsdir/carddecks/decks/*
%_kde_appsdir/carddecks/cards-aisleriot/*
%_kde_appsdir/carddecks/cards-default/*
%_kde_appsdir/carddecks/cards-dondorf-whist-b/*
%_kde_appsdir/carddecks/cards-gdkcard-bonded/*
%_kde_appsdir/carddecks/cards-hard-a-port/*
%_kde_appsdir/carddecks/cards-konqi-modern/*
%_kde_appsdir/carddecks/cards-penguins/*
%_kde_appsdir/carddecks/cards-spaced/*
%_kde_appsdir/carddecks/cards-warwick/*
%_kde_appsdir/carddecks/cards-xskat-french/*
%_kde_appsdir/carddecks/cards-xskat-german/*
%_kde_appsdir/carddecks/svg-classic/*
%_kde_appsdir/carddecks/svg-dondorf/*
%_kde_appsdir/carddecks/svg-gm-paris/*
%_kde_appsdir/carddecks/svg-nicu-ornamental/*
%_kde_appsdir/carddecks/svg-nicu-white/*
%_kde_iconsdir/oxygen/*/actions/endturn.png
%_kde_iconsdir/oxygen/*/actions/lastmoves.png
%_kde_iconsdir/oxygen/*/actions/legalmoves.png

%package -n %lib_name-devel
Summary:	Headers files for kdegames
Group:		Development/KDE and Qt

Provides:   %name-devel = %epoch:%version-%release
Provides:   %lib_name_orig-devel = %epoch:%version-%release
%define mini_release %mkrel 0.%revision.1
Requires:	kdelibs4-devel >= %version-%mini_release

%description -n %lib_name-devel
Headers files needed to build applications based on kdegames applications.

%post -n %lib_name-devel -p /sbin/ldconfig

%postun -n %lib_name-devel -p /sbin/ldconfig


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
Summary:        KGoldrunner, a game of action and puzzle solving.
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kgoldrunner4

%description -n kde4-kgoldrunner

KGoldrunner, a game of action and puzzle solving. 
Run through the maze, dodge your enemies, collect 
all the gold and climb up to the next level.

%post -n kde4-kgoldrunner
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kgoldrunner
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor


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
Summary:        Backgammon Game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kbackgammon4

%description -n kde4-kbackgammon
kbackgammon: play backgammon against a local human player, via a
               game server or against GNU Backgammon (not included)

%post -n kde4-kbackgammon
/sbin/ldconfig
%update_icon_cache hicolor

%postun -n kde4-kbackgammon
/sbin/ldconfig
%clean_icon_cache hicolor


%files -n kde4-kbackgammon
%defattr(-,root,root)
%_kde_bindir/kbackgammon
%_kde_datadir/applications/kde4/kbackgammon.desktop
%dir %_kde_docdir/HTML/en/kbackgammon
%doc %_kde_docdir/HTML/en/kbackgammon/board.png
%doc %_kde_docdir/HTML/en/kbackgammon/index.cache.bz2
%doc %_kde_docdir/HTML/en/kbackgammon/index.docbook
%_kde_iconsdir/hicolor/*/apps/kbackgammon*
%_kde_appsdir/kbackgammon/kbackgammonui.rc
%_kde_appsdir/kbackgammon/pics/*
%dir %_kde_appsdir/kbackgammon/sounds
%_kde_appsdir/kbackgammon/sounds/*
%_kde_appsdir/kbackgammon/kbackgammon.notifyrc

#-----------------------------------------------------------------------------

%package -n     kde4-katomic
Summary:        Build complex atoms with a minimal amount of moves
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       katomic4

%description -n kde4-katomic
katomic: build complex atoms with a minimal amount of moves

%post -n kde4-katomic
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-katomic
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor


%files -n kde4-katomic
%defattr(-,root,root)
%_kde_bindir/katomic
%_kde_datadir/applications/kde4/katomic.desktop
%doc %_kde_docdir/HTML/en/katomic/index.cache.bz2
%doc%doc %_kde_docdir/HTML/en/katomic/index.docbook
%_kde_iconsdir/hicolor/*/apps/katomic.png
%_kde_appsdir/katomic/levels/*
%_kde_appsdir/katomic/pics/default_theme.svgz
%_kde_appsdir/katomic/katomicui.rc

#-----------------------------------------------------------------------------

%package -n     kde4-kblackbox
Summary:        Find atoms in a grid by shooting electrons
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kblackbox4

%description -n kde4-kblackbox
kblackbox: find atoms in a grid by shooting electrons

%post -n kde4-kblackbox
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kblackbox
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor


%files -n kde4-kblackbox
%defattr(-,root,root)
%_kde_bindir/kblackbox
%_kde_datadir/applications/kde4/kblackbox.desktop
%_kde_appsdir/kblackbox/kblackboxui.rc
%_kde_appsdir/kblackbox/pics/kblackbox.svgz
%dir %_kde_docdir/HTML/en/kblackbox
%doc %_kde_docdir/HTML/en/kblackbox/index.cache.bz2
%doc %_kde_docdir/HTML/en/kblackbox/index.docbook
%doc %_kde_docdir/HTML/en/kblackbox/kblackboxtbar.png
%_kde_iconsdir/hicolor/*/apps/kblackbox.png

#-----------------------------------------------------------------------------

%package -n     kde4-ktuberling
Summary:        KTuberling: "potato editor" game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ktuberling4

%description -n kde4-ktuberling

KTuberling is a "potato editor" game intended for small 
children and adults who remain young at heart. The game 
has no winner; the only purpose is to make the funniest 
faces you can.

%post -n kde4-ktuberling
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-ktuberling
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
%doc %_kde_docdir/HTML/en/ktuberling/*.png
%doc %_kde_docdir/HTML/en/ktuberling/index.cache.bz2
%doc %_kde_docdir/HTML/en/ktuberling/index.docbook
%doc %_kde_docdir/HTML/en/ktuberling/technical-reference.docbook
%_kde_iconsdir/hicolor/*/apps/ktuberling.png

#-----------------------------------------------------------------------------

%package -n     kde4-kbounce
Summary:        Claim areas and don't get disturbed
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kbounce4

%description -n kde4-kbounce
kbounce: claim areas and don't get disturbed

%files -n kde4-kbounce
%defattr(-,root,root)
%_kde_bindir/kbounce
%_kde_datadir/applications/kde4/kbounce.desktop
%_kde_appsdir/kbounce/kbounceui.rc
%_kde_appsdir/kbounce/themes/*
%dir %_kde_datadir/apps/kbounce/sounds
%_kde_datadir/apps/kbounce/sounds/*.au
%doc %_kde_docdir/HTML/en/kbounce/index.cache.bz2
%doc %_kde_docdir/HTML/en/kbounce/index.docbook
%doc %_kde_docdir/HTML/en/kbounce/jezball_corridor1.png
%doc %_kde_docdir/HTML/en/kbounce/jezball_corridor2.png
%doc %_kde_docdir/HTML/en/kbounce/jezball_newWall.png

#-----------------------------------------------------------------------------

%package -n     kde4-kspaceduel
Summary:        Two player game with shooting spaceships flying around a sun
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kspaceduel4

%description -n kde4-kspaceduel
kspaceduel: two player game with shooting spaceships flying around a sun

%post -n kde4-kspaceduel
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kspaceduel
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-kspaceduel
%defattr(-,root,root)
%_kde_bindir/kspaceduel
%_kde_datadir/applications/kde4/kspaceduel.desktop
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
%doc %_kde_docdir/HTML/en/kspaceduel/index.cache.bz2
%doc %_kde_docdir/HTML/en/kspaceduel/index.docbook
%doc %_kde_docdir/HTML/en/kspaceduel/kspaceduel3.png
%_kde_iconsdir/hicolor/*/apps/kspaceduel.png

#-----------------------------------------------------------------------------

%package -n     kde4-kreversi
Summary:        Old reversi board game, also known as othello
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kreversi4

%description -n kde4-kreversi
kreversi: the old reversi board game, also known as othello

%post -n kde4-kreversi
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kreversi
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
Summary:        A golf game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kolf4

%description -n kde4-kolf
kolf: a golf game

%post -n kde4-kolf
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kolf
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
%doc %_kde_docdir/HTML/en/kolf/index.cache.bz2
%doc %_kde_docdir/HTML/en/kolf/index.docbook
%_kde_datadir/icons/hicolor/*/apps/kolf.png

#-----------------------------------------------------------------------------

%package -n     kde4-konquest
Summary:        Conquer the planets of your enemy
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       konquest4

%description -n kde4-konquest
konquest: conquer the planets of your enemy

%post -n kde4-konquest
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-konquest
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-konquest
%defattr(-,root,root)
%_kde_bindir/konquest
%_kde_datadir/applications/kde4/konquest.desktop
%_kde_appsdir/konquest/konquestui.rc
%_kde_appsdir/konquest/pics
%_kde_appsdir/konquest/pics/konquest-splash.png
%_kde_appsdir/konquest/pics/*
%doc %_kde_docdir/HTML/en/konquest/index.cache.bz2
%doc %_kde_docdir/HTML/en/konquest/index.docbook
%_kde_datadir/icons/hicolor/*/apps/konquest.png


#-----------------------------------------------------------------------------

%package -n     kde4-ksame
Summary:        Collect pieces of the same color
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksame4

%description -n kde4-ksame
ksame: collect pieces of the same color

%post -n kde4-ksame
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-ksame
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-ksame
%defattr(-,root,root)
%_kde_bindir/ksame
%_kde_appsdir/ksame/ksameui.rc
%_kde_datadir/applications/kde4/ksame.desktop
%_kde_appsdir/ksame/pics/default_theme.svgz
%dir %_kde_docdir/HTML/en/ksame
%doc %_kde_docdir/HTML/en/ksame/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksame/index.docbook
%_kde_datadir/icons/hicolor/*/apps/ksame.png

#-----------------------------------------------------------------------------

%package -n     kde4-kmahjongg
Summary:        A tile laying patience
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kmahjongg4

%description -n kde4-kmahjongg
Kmahjongg: a tile laying patience

%post -n kde4-kmahjongg
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kmahjongg
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
Summary:        Battleship game with built-in game server
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kbattleship4

%description -n kde4-kbattleship
kbattleship: battleship game with built-in game server

%post -n kde4-kbattleship
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kbattleship
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-kbattleship
%defattr(-,root,root)
%_kde_bindir/kbattleship
%_kde_datadir/applications/kde4/kbattleship.desktop
%doc %_kde_docdir/HTML/en/kbattleship/index.cache.bz2
%doc %_kde_docdir/HTML/en/kbattleship/index.docbook
%_kde_iconsdir/hicolor/*/apps/kbattleship.png
%_kde_appsdir/kbattleship/kbattleshipui.rc
%_kde_appsdir/kbattleship/pictures/default_theme.svgz
%_kde_appsdir/kbattleship/sounds/*

#-----------------------------------------------------------------------------

%package -n     kde4-kiriki
Summary:        
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kiriki4

%description -n kde4-kiriki

Kiriki is a dice game, written for KDE 4. 
It is a clone of Gnome Tali (gtali) that is a clone of Yahtzee!

%post -n kde4-kiriki
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kiriki
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-kiriki
%defattr(-,root,root)
%_kde_bindir/kiriki
%_kde_datadir/applications/kde4/kiriki.desktop
%doc %_kde_docdir/HTML/en/kiriki/index.cache.bz2
%doc %_kde_docdir/HTML/en/kiriki/index.docbook
%_kde_iconsdir/hicolor/*/apps/kiriki.png
%_kde_appsdir/kiriki/images/*
%_kde_appsdir/kiriki/kirikiui.rc

#-----------------------------------------------------------------------------

%package -n     kde4-ksudoku
Summary:        KSudoku - Play, create and solve sudoku grids 
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksudoku4

%description -n kde4-ksudoku

The word Sudoku means "single number in an alloted place" in Japanese. These
are the basic rules. Every sudoku Sudoku is a square of 81 cells divided into
9 columns and 9 rows and in 9 subsquares (3x3) of 9 cells each. Solving takes
usually from 10 to 30 minutes, depending on puzzle level, your skill and
experience.

Some cells are filled with a number at the beginnning: the remaining are to
be filled by the player using numbers from 1 to 9, without repeating a number
twice on each column, row or subsuquare (each of them must contain only
one 1, one 2, one 3, and so on). The game requires logic and patience.
The numerals in Sudoku puzzles are used for convenience (for example in 16x16
board we use letters): arithmetic relationships between numbers are irrelevant.

This program supports also 16x16 games with numbers from 1 to 16 and 256
cells with 16 cols, rows and subsquares! (if normal sudoku are not enough for
you).

More information at http://en.wikipedia.org/wiki/Sudoku

%post-n kde4-ksudoku
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun-n kde4-ksudoku
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
%doc %_kde_docdir/HTML/en/ksudoku/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksudoku/index.docbook
%_kde_iconsdir/hicolor/*/apps/ksudoku.png

#-----------------------------------------------------------------------------

%package -n     kde4-bovo
Summary:        Bovo: classic pen and paper game
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       bovo4

%description -n kde4-bovo

Bovo is a KDE 4 game, modeled upon a classic pen and paper game, 
where you try to connect five in a row prior to your opponent.

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
%doc %_kde_docdir/HTML/en/bovo/index.cache.bz2
%doc %_kde_docdir/HTML/en/bovo/index.docbook

#-----------------------------------------------------------------------------

%package -n     kde4-kjumpingcube
Summary:        kjumpingcube: a tactical game for number-crunchers
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kjumpingcube4

%description -n kde4-kjumpingcube

KJumpingCube is a tactical one or two-player game. The playing field 
consists of squares that contains points which can be increased. By 
this you can gain more fields and finally win the board over.

%post -n kde4-kjumpingcube
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kjumpingcube
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-kjumpingcube
%defattr(-,root,root)
%_kde_bindir/kjumpingcube
%_kde_datadir/applications/kde4/kjumpingcube.desktop
%_kde_appsdir/kjumpingcube/kjumpingcubeui.rc
%_kde_appsdir/kjumpingcube/pics/default.desktop
%_kde_appsdir/kjumpingcube/pics/default.svg
%doc %_kde_docdir/HTML/en/kjumpingcube/index.cache.bz2
%doc %_kde_docdir/HTML/en/kjumpingcube/index.docbook
%_kde_iconsdir/hicolor/*/apps/kjumpingcube.png

#-----------------------------------------------------------------------------

%package -n     kde4-klines
Summary:        Place 5 equal pieces together, but wait, there are 3 new ones
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       klines4

%description -n kde4-klines
klines: place 5 equal pieces together, but wait, there are 3 new ones

%post -n kde4-klines
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-klines
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-klines
%defattr(-,root,root)
%_kde_bindir/klines
%_kde_datadir/applications/kde4/klines.desktop
%_kde_appsdir/klines/klinesui.rc
%_kde_appsdir/klines/themes/default.desktop
%_kde_appsdir/klines/themes/klines.svgz
%doc %_kde_docdir/HTML/en/klines/index.cache.bz2
%doc %_kde_docdir/HTML/en/klines/index.docbook
%_kde_iconsdir/hicolor/*/apps/klines.png

#-----------------------------------------------------------------------------

%package -n     kde4-kmines
Summary:        The classical mine sweeper
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kmines4

%description -n kde4-kmines
kmines: the classical mine sweeper

%post -n kde4-kmines
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kmines
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
%doc %_kde_docdir/HTML/en/kmines/index.cache.bz2
%doc %_kde_docdir/HTML/en/kmines/index.docbook
%doc %_kde_docdir/HTML/en/kmines/kmines1.png
%doc %_kde_docdir/HTML/en/kmines/kmines2.png
%_kde_iconsdir/hicolor/*/apps/kmines.png

#-----------------------------------------------------------------------------

%package -n     kde4-knetwalk
Summary:        Turn the board pieces to get all computers connected. 
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       knetwalk4

%description -n kde4-knetwalk

Turn the board pieces to get all computers connected.

%post -n kde4-knetwalk
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-knetwalk
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
%_kde_iconsdir/hicolor/*/apps/knetwalk.png

#-----------------------------------------------------------------------------

%package -n     kde4-kpat
Summary:        Several patience card games
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kpat4

%description -n kde4-kpat
kpat: several patience card games

%post -n kde4-kpat
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kpat
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-kpat
%defattr(-,root,root)
%_kde_bindir/kpat
%_kde_datadir/applications/kde4/kpat.desktop
%_kde_appsdir/kpat/backgrounds/background.svg
%_kde_appsdir/kpat/kpatui.rc
%_kde_appsdir/kpat/pile.svg
%_kde_appsdir/kpat/won.svg
%doc %_kde_docdir/HTML/en/kpat/clubs.png
%doc %_kde_docdir/HTML/en/kpat/diamonds.png
%doc %_kde_docdir/HTML/en/kpat/hearts.png
%doc %_kde_docdir/HTML/en/kpat/index.cache.bz2
%doc %_kde_docdir/HTML/en/kpat/index.docbook
%doc %_kde_docdir/HTML/en/kpat/man-kpat.6.docbook
%doc %_kde_docdir/HTML/en/kpat/playfield.png
%doc %_kde_docdir/HTML/en/kpat/spades.png
%_kde_iconsdir/hicolor/*/apps/kpat.png

#-----------------------------------------------------------------------------

%package -n     kde4-kshisen
Summary:        Patience game where you take away all pieces
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kshisen4

%description -n kde4-kshisen
Kshisen: patience game where you take away all pieces

%post -n kde4-kshisen
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kshisen
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-kshisen
%defattr(-,root,root)
%_kde_bindir/kshisen
%_kde_datadir/applications/kde4/kshisen.desktop
%_kde_appsdir/kshisen/kshisenui.rc
%doc %_kde_docdir/HTML/en/kshisen/index.cache.bz2
%doc %_kde_docdir/HTML/en/kshisen/index.docbook
%doc %_kde_docdir/HTML/en/kshisen/kshisen-configuration.png
%doc %_kde_docdir/HTML/en/kshisen/score-formula.png
%_kde_iconsdir/hicolor/*/apps/kshisen.png

#-----------------------------------------------------------------------------

%package -n     kde4-ksquares
Summary:        KSquares: an implementation of the popular paper based game squares
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksquares4

%description -n kde4-ksquares
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%post -n kde4-ksquares
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor
%update_icon_cache scalable

%postun -n kde4-ksquares
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor
%clean_icon_cache scalable

%files -n kde4-ksquares
%defattr(-,root,root)
%_kde_bindir/ksquares
%_kde_datadir/applications/kde4/ksquares.desktop
%_kde_appsdir/ksquares/ksquaresui.rc
%dir %_kde_docdir/HTML/en/ksquares
%doc %_kde_docdir/HTML/en/ksquares/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksquares/index.docbook
%_kde_iconsdir/hicolor/*/apps/ksquares.png
%_kde_iconsdir/hicolor/scalable/actions/ksquares_ai.svgz
%_kde_iconsdir/hicolor/scalable/actions/ksquares_display.svgz

#-----------------------------------------------------------------------------

%package -n     kde4-kwin4
Summary:        Place 4 pieces in a row
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       kwin44

%description -n kde4-kwin4
kwin4: place 4 pieces in a row

%post -n kde4-kwin4
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-kwin4
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

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
%dir %_kde_docdir/HTML/en/kwin4
%doc %_kde_docdir/HTML/en/kwin4/index.cache.bz2
%doc %_kde_docdir/HTML/en/kwin4/index.docbook
%_kde_iconsdir/hicolor/*/apps/kwin4.png

#-----------------------------------------------------------------------------

%package -n     kde4-lskat
Summary:        Lieutnant skat
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       lskat4

%description -n kde4-lskat
lskat: lieutnant skat

%post -n kde4-lskat
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-lskat
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-lskat
%defattr(-,root,root)
%_kde_bindir/lskat
%_kde_datadir/applications/kde4/lskat.desktop
%_kde_appsdir/lskat/grafix/default.rc
%_kde_appsdir/lskat/grafix/default.svg
%_kde_appsdir/lskat/lskatui.rc
%dir %_kde_docdir/HTML/en/lskat
%doc %_kde_docdir/HTML/en/lskat/index.cache.bz2
%doc %_kde_docdir/HTML/en/lskat/index.docbook
%_kde_iconsdir/hicolor/*/apps/lskat.png

#-----------------------------------------------------------------------------

%package -n     kde4-ksirtet
Summary:        Ksirtet: clone of the well known Tetris game family
Group:          Graphical desktop/KDE
Requires:       kdegames4-core

Provides:       ksirtet4

%description -n kde4-ksirtet
KSirtet is a clone of the well known Tetris game family. The game
allows multiplayer duels including games against a computer player.
Everybody knowing Tetris should immediately feel at home with this
game.

%post -n kde4-ksirtet
/sbin/ldconfig
%{update_desktop_database}
%update_icon_cache hicolor

%postun -n kde4-ksirtet
/sbin/ldconfig
%{clean_desktop_database}
%clean_icon_cache hicolor

%files -n kde4-ksirtet
%defattr(-,root,root)
%_kde_datadir/applications/kde4/ksirtet.desktop
%_kde_appsdir/ksirtet/ksirtet.notifyrc
%_kde_appsdir/ksirtet/ksirtetui.rc
%dir %_kde_docdir/HTML/en/ksirtet
%doc %_kde_docdir/HTML/en/ksirtet/index.cache.bz2
%doc %_kde_docdir/HTML/en/ksirtet/index.docbook
%_kde_iconsdir/hicolor/*/apps/ksirtet.png

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

%clean
rm -fr %buildroot

