# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kdegames4
Summary:	KDE - Games
Version:	4.9.4
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://games.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdegames-%{version}.tar.xz
Source1:	%{name}.rpmlintrc
Patch0:		kdegames-4.8.97-l10n-ru.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	libxml2-utils
BuildRequires:	python-qt4
BuildRequires:	python-kde4
BuildRequires:	python-twisted-core
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(sqlite3)
Suggests:	katomic
Suggests:	kbattleship
Suggests:	kblackbox
Suggests:	kbounce
Suggests:	klines
Suggests:	kmahjongg
Suggests:	kmines
Suggests:	kolf
Suggests:	konquest
Suggests:	kpat
Suggests:	kreversi
Suggests:	klickety
Suggests:	kshisen
Suggests:	kspaceduel
Suggests:	ktuberling
Suggests:	kfourinline
Suggests:	lskat
Suggests:	ksudoku
Suggests:	kgoldrunner
Suggests:	ktuberling
Suggests:	kiriki
Suggests:	kjumpingcube
Suggests:	bovo
Suggests:	ksquares
Suggests:	knetwalk
Suggests:	kollision
Suggests:	kubrick
Suggests:	kdiamond
Suggests:	kblocks
Suggests:	ksirk
Suggests:	kbreakout
Suggests:	kapman
Suggests:	killbots
Suggests:	bomber
Suggests:	ktron
Suggests:	kdesnake
Suggests:	granatier
Suggests:	kigo
Suggests:	palapeli

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
 - katomic: build complex atoms with a minimal amount of moves
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
 - kshisen: patience game where you take away all pieces
 - kspaceduel: two player game with shooting spaceships flying around a sun
 - ktuberling: kids game: make your own potato (NO french fries!)
 - kfourinline: place 4 pieces in a row
 - Lskat: lieutnant skat
 - Ksudoku: Play, create and solve sudoku grids
 - KGoldrunner: a game of action and puzzle solving.
 - KTuberling: "potato editor" game
 - Kiriki: Close of Yahtzee
 - Kjumpingcube: a tactical game for number-crunchers
 - Bovo: classic pen and paper game
 - KSquares: an implementation of the popular paper based game squares
 - Knetwalk: Turn the board pieces to get all computers connected

%files


#--------------------------------------------------------------------

%package core
Summary:	Common files needed by Kdegames4 packages
Group:		Graphical desktop/KDE
Requires:	kdebase4-runtime

%description core
Common files needed by Kdegames4 packages

%files core
%{_kde_appsdir}/carddecks
%{_kde_configdir}/kcardtheme.knsrc
%{_kde_iconsdir}/oxygen/*/actions/lastmoves.*
%{_kde_iconsdir}/oxygen/*/actions/legalmoves.*
%{_kde_appsdir}/kconf_update/kgthemeprovider-migration.upd

#-----------------------------------------------------------------------------

%package -n kgoldrunner
Summary:	KGoldrunner, a game of action and puzzle solving
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kgoldrunner
Requires:	kdegames4-core

%description -n kgoldrunner
KGoldrunner, a game of action and puzzle solving.
Run through the maze, dodge your enemies, collect
all the gold and climb up to the next level.

%files -n kgoldrunner
%{_kde_bindir}/kgoldrunner
%{_kde_applicationsdir}/KGoldrunner.desktop
%{_kde_configdir}/kgoldrunner.knsrc
%{_kde_appsdir}/kgoldrunner
%{_kde_docdir}/*/*/kgoldrunner
%{_kde_iconsdir}/hicolor/*/apps/kgoldrunner.png

#-----------------------------------------------------------------------------

%package -n kapman
Summary:	A Pac-Man clone
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kapman
Kapman is a Pac-Man clone.

%files -n kapman
%{_kde_bindir}/kapman
%{_kde_applicationsdir}/kapman.desktop
%{_kde_appsdir}/kapman
%{_kde_docdir}/*/*/kapman
%{_kde_iconsdir}/hicolor/*/apps/kapman.*
%{_kde_datadir}/sounds/kapman

#-----------------------------------------------------------------------------

%package -n katomic
Summary:	Build complex atoms with a minimal amount of moves
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=katomic
Requires:	kdegames4-core

%description -n katomic
katomic: build complex atoms with a minimal amount of moves

%files -n katomic
%{_kde_bindir}/katomic
%{_kde_applicationsdir}/katomic.desktop
%{_kde_docdir}/*/*/katomic
%{_kde_iconsdir}/hicolor/*/apps/katomic.png
%{_kde_appsdir}/katomic
%{_kde_configdir}/katomic.knsrc
%{_kde_appsdir}/kconf_update/katomic-levelset-upd.pl
%{_kde_appsdir}/kconf_update/katomic-levelset.upd

#-----------------------------------------------------------------------------

%package -n kblackbox
Summary:	Find atoms in a grid by shooting electrons
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kblackbox
Requires:	kdegames4-core

%description -n kblackbox
kblackbox: find atoms in a grid by shooting electrons

%files -n kblackbox
%{_kde_bindir}/kblackbox
%{_kde_applicationsdir}/kblackbox.desktop
%{_kde_appsdir}/kblackbox
%{_kde_docdir}/*/*/kblackbox
%{_kde_iconsdir}/hicolor/*/apps/kblackbox.png

#-----------------------------------------------------------------------------

%package -n ktuberling
Summary:	KTuberling: "potato editor" game
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ktuberling
Requires:	kdegames4-core

%description -n ktuberling
KTuberling is a "potato editor" game intended for small 
children and adults who remain young at heart. The game 
has no winner; the only purpose is to make the funniest 
faces you can.

%files -n ktuberling
%{_kde_bindir}/ktuberling
%{_kde_applicationsdir}/ktuberling.desktop
%{_kde_appsdir}/ktuberling
%{_kde_docdir}/*/*/ktuberling
%{_kde_iconsdir}/hicolor/*/apps/ktuberling.png
%{_kde_iconsdir}/hicolor/*/mimetypes/application-x-tuberling.png

#-----------------------------------------------------------------------------

%package -n kbounce
Summary:	Claim areas and don't get disturbed
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kbounce
Requires:	kdegames4-core

%description -n kbounce
kbounce: claim areas and don't get disturbed

%files -n kbounce
%{_kde_bindir}/kbounce
%{_kde_applicationsdir}/kbounce.desktop
%{_kde_appsdir}/kbounce
%{_kde_iconsdir}/*/*/apps/kbounce*
%{_kde_docdir}/*/*/kbounce

#-----------------------------------------------------------------------------

%package -n killbots
Summary:	KDE port of the classic BSD console game robots
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n killbots
Killbots is a KDE port of the classic BSD console game robots.

%files -n killbots
%{_kde_bindir}/killbots
%{_kde_applicationsdir}/killbots.desktop
%{_kde_appsdir}/killbots
%{_kde_datadir}/config.kcfg/killbots.kcfg
%{_kde_docdir}/*/*/killbots
%{_kde_iconsdir}/hicolor/*/apps/killbots.*

#-----------------------------------------------------------------------------

%package -n kspaceduel
Summary:	Two player game with shooting spaceships flying around a sun
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kspaceduel
Requires:	kdegames4-core

%description -n kspaceduel
kspaceduel: two player game with shooting spaceships flying around a sun

%files -n kspaceduel
%{_kde_bindir}/kspaceduel
%{_kde_applicationsdir}/kspaceduel.desktop
%{_kde_appsdir}/kspaceduel
%{_kde_docdir}/*/*/kspaceduel
%{_kde_iconsdir}/hicolor/*/apps/kspaceduel.png
%{_kde_datadir}/config.kcfg/kspaceduel.kcfg

#-----------------------------------------------------------------------------

%package -n kreversi
Summary:	Old reversi board game, also known as othello
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kreversi
Requires:	kdegames4-core

%description -n kreversi
kreversi: the old reversi board game, also known as othello

%files -n kreversi
%{_kde_bindir}/kreversi
%{_kde_applicationsdir}/kreversi.desktop
%{_kde_appsdir}/kreversi
%{_kde_iconsdir}/hicolor/*/apps/kreversi.png
%{_kde_docdir}/*/*/kreversi

#-----------------------------------------------------------------------------

%package -n kolf
Summary:	A golf game
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kolf
Requires:	kdegames4-core

%description -n kolf
Kolf is a miniature golf game with 2d top-down view. Courses are dynamic,
and up to 10 people can play at once in competition. Kolf comes equipped
with a variety of playgrounds and tutorial courses.

%files -n kolf
%{_kde_bindir}/kolf
%{_kde_applicationsdir}/kolf.desktop
%{_kde_appsdir}/kolf
%{_kde_docdir}/*/*/kolf
%{_kde_iconsdir}/hicolor/*/apps/kolf.png

#-----------------------------------------------------------------------------

%package -n konquest
Summary:	Conquer the planets of your enemy
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=konquest
Requires:	kdegames4-core

%description -n konquest
konquest: conquer the planets of your enemy

%files -n konquest
%{_kde_bindir}/konquest
%{_kde_applicationsdir}/konquest.desktop
%{_kde_appsdir}/konquest
%{_kde_docdir}/*/*/konquest
%{_kde_iconsdir}/hicolor/*/apps/konquest.png

#-----------------------------------------------------------------------------

%package -n klickety
Summary:	An adaptation of the Clickomania game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core
Provides:	ksame = %{EVRD}
Obsoletes:	ksame < 1:4.5.74

%description -n klickety
Klickety is an adaptation of the Clickomania game.
The rules are similar to those of the Same game: your goal is to clear
the board by clicking on groups to destroy them.

%files -n klickety
%{_kde_bindir}/klickety
%{_kde_applicationsdir}/klickety.desktop
%{_kde_applicationsdir}/ksame.desktop
%{_kde_appsdir}/klickety
%{_kde_appsdir}/kconf_update/klickety.upd
%{_kde_appsdir}/kconf_update/klickety-2.0-inherit-ksame-highscore.pl
%{_kde_docdir}/HTML/en/klickety
%{_kde_iconsdir}/*/*/apps/klickety.*
%{_kde_iconsdir}/*/*/apps/ksame.*

#-----------------------------------------------------------------------------

%package -n kmahjongglib
Summary:	Common files for kmahjongg
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kmahjongglib
Common files for kmahjongg.

%files -n kmahjongglib
%{_kde_appsdir}/kmahjongglib

#-----------------------------------------------------------------------------

%package -n kmahjongg
Summary:	A tile laying patience
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kmahjongg
Requires:	kdegames4-core

%description -n kmahjongg
Kmahjongg: a tile laying patience

%files -n kmahjongg
%{_kde_bindir}/kmahjongg
%{_kde_applicationsdir}/kmahjongg.desktop
%{_kde_appsdir}/kmahjongg
%{_kde_docdir}/*/*/kmahjongg
%{_kde_iconsdir}/hicolor/*/apps/kmahjongg.*
%{_kde_datadir}/config.kcfg/kmahjongg.kcfg

#-----------------------------------------------------------------------------

%package -n kbattleship
Summary:	Battleship game with built-in game server
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kbattleship
Requires:	kdegames4-core

%description -n kbattleship
kbattleship: battleship game with built-in game server

%files -n kbattleship
%{_kde_bindir}/kbattleship
%{_kde_applicationsdir}/kbattleship.desktop
%{_kde_docdir}/*/*/kbattleship
%{_kde_iconsdir}/hicolor/*/apps/kbattleship.png
%{_kde_appsdir}/kbattleship
%{_kde_services}/kbattleship.protocol

#-----------------------------------------------------------------------------

%package -n kiriki
Summary:	Kiriki: Close of Yahtzee 
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kiriki
Requires:	kdegames4-core

%description -n kiriki
Kiriki is a dice game, written for KDE 4.
It is a clone of Gnome Tali (gtali) that is a clone of Yahtzee!

%files -n kiriki
%{_kde_bindir}/kiriki
%{_kde_applicationsdir}/kiriki.desktop
%{_kde_docdir}/*/*/kiriki
%{_kde_iconsdir}/hicolor/*/apps/kiriki.png
%{_kde_appsdir}/kiriki

#-----------------------------------------------------------------------------

%package -n ksudoku
Summary:	KSudoku - Play, create and solve sudoku grids 
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ksudoku
Requires:	kdegames4-core

%description -n ksudoku
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

%files -n ksudoku
%{_kde_bindir}/ksudoku
%{_kde_applicationsdir}/ksudoku.desktop
%{_kde_appsdir}/ksudoku
%{_kde_configdir}/ksudokurc
%{_kde_iconsdir}/hicolor/*/apps/ksudoku.png
%{_kde_docdir}/*/*/ksudoku

#-----------------------------------------------------------------------------

%package -n bovo
Summary:	Bovo: classic pen and paper game
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=bovo
Requires:	kdegames4-core

%description -n bovo
Bovo is a KDE 4 game, modeled upon a classic pen and paper game, 
where you try to connect five in a row prior to your opponent.

%files -n bovo
%{_kde_bindir}/bovo
%{_kde_applicationsdir}/bovo.desktop
%{_kde_appsdir}/bovo
%{_kde_docdir}/*/*/bovo
%{_kde_iconsdir}/hicolor/*/apps/bovo.*

#-----------------------------------------------------------------------------

%package -n kjumpingcube
Summary:	kjumpingcube: a tactical game for number-crunchers
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kjumpingcube
Requires:	kdegames4-core

%description -n kjumpingcube
KJumpingCube is a tactical one or two-player game. The playing field 
consists of squares that contains points which can be increased. By 
this you can gain more fields and finally win the board over.

%files -n kjumpingcube
%{_kde_bindir}/kjumpingcube
%{_kde_applicationsdir}/kjumpingcube.desktop
%{_kde_appsdir}/kjumpingcube
%{_kde_datadir}/config.kcfg/kjumpingcube.kcfg
%{_kde_docdir}/*/*/kjumpingcube
%{_kde_iconsdir}/hicolor/*/apps/kjumpingcube.png

#-----------------------------------------------------------------------------

%package -n klines
Summary:	Place 5 equal pieces together, but wait, there are 3 new ones
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=klines
Requires:	kdegames4-core

%description -n klines
klines: place 5 equal pieces together, but wait, there are 3 new ones

%files -n klines
%{_kde_bindir}/klines
%{_kde_applicationsdir}/klines.desktop
%{_kde_appsdir}/klines
%{_kde_docdir}/*/*/klines
%{_kde_iconsdir}/hicolor/*/apps/klines.png
%{_kde_datadir}/config.kcfg/klines.kcfg

#-----------------------------------------------------------------------------

%package -n kmines
Summary:	The classical mine sweeper
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kmines
Requires:	kdegames4-core

%description -n kmines
kmines: the classical mine sweeper

%files -n kmines
%{_kde_bindir}/kmines
%{_kde_applicationsdir}/kmines.desktop
%{_kde_appsdir}/kmines
%{_kde_configdir}/kmines.knsrc
%{_kde_docdir}/*/*/kmines
%{_kde_iconsdir}/hicolor/*/apps/kmines.png

#-----------------------------------------------------------------------------

%package -n knetwalk
Summary:	Turn the board pieces to get all computers connected 
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=knetwalk
Requires:	kdegames4-core

%description -n knetwalk
Turn the board pieces to get all computers connected.

%files -n knetwalk
%{_kde_bindir}/knetwalk
%{_kde_applicationsdir}/knetwalk.desktop
%{_kde_appsdir}/knetwalk
%{_kde_docdir}/*/*/knetwalk
%{_kde_iconsdir}/hicolor/*/apps/knetwalk.*

#-----------------------------------------------------------------------------

%package -n kpat
Summary:	Several patience card games
Group:		Graphical desktop/KDE
Requires:	kdegames4-core
Conflicts:	kdegames4-devel < 1:4.5.71-0.svn1184269.2

%description -n kpat
kpat: several patience card games

%files -n kpat
%{_kde_bindir}/kpat
%{_kde_libdir}/libkcardgame.so
%{_kde_applicationsdir}/kpat.desktop
%{_kde_appsdir}/kpat
%{_kde_datadir}/config.kcfg/kpat.kcfg
%{_kde_configdir}/kpat.knsrc
%{_kde_docdir}/*/*/kpat
%{_kde_iconsdir}/hicolor/*/apps/kpat.png
%{_datadir}/mime/packages/kpatience.xml

#----------------------------------------------------------------------------

%package -n kajongg
Summary:	kajongg : Majongg game for KDE
Group:		Graphical desktop/KDE
Requires:	kdegames4-core
Requires:	python-kde4
Requires:	python-twisted-core
Requires:	qt4-database-plugin-sqlite

%description -n kajongg
kajongg : Majongg game for KDE

%files -n kajongg
%{_kde_bindir}/kajongg
%{_kde_bindir}/kajonggserver
%{_kde_applicationsdir}/kajongg.desktop
%{_kde_appsdir}/kajongg
%{_kde_docdir}/HTML/en/kajongg
%{_kde_iconsdir}/hicolor/*/*/*kajongg*

#-----------------------------------------------------------------------------

%package -n kshisen
Summary:	Patience game where you take away all pieces
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kshisen
Requires:	kdegames4-core

%description -n kshisen
Kshisen: patience game where you take away all pieces

%files -n kshisen
%{_kde_bindir}/kshisen
%{_kde_applicationsdir}/kshisen.desktop
%{_kde_appsdir}/kshisen
%{_kde_datadir}/sounds/kshisen
%{_kde_datadir}/config.kcfg/kshisen.kcfg
%{_kde_iconsdir}/hicolor/*/apps/kshisen*
%{_kde_docdir}/*/*/kshisen

#-----------------------------------------------------------------------------

%package -n ktron
Summary:	Simple Tron clone
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ktron
Requires:	kdegames4-core

%description -n ktron
Well known from the famous movie, KTron is a popular computer 
game for two players. In a fast action sequence both players 
have to move and avoid colliding with any walls, the opponent 
as well as the own path. The player colliding first looses the 
game.

%files -n ktron
%{_kde_bindir}/ktron
%{_kde_applicationsdir}/ktron.desktop
%{_kde_appsdir}/ktron
%{_kde_datadir}/config.kcfg/ktron.kcfg
%{_kde_configdir}/ktron.knsrc
%{_kde_iconsdir}/hicolor/*/*/ktron.png
%{_kde_docdir}/HTML/en/ktron

#-----------------------------------------------------------------------------

%package -n kdesnake
Summary:	snake race played against the computer
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kdesnake
Requires:	kdegames4-core

%description -n kdesnake
KSnake Race is a fast action game where you steer a snake 
which has to eat food. While eating the snake grows. But 
once a player collides with the other snake or the wall 
the game is lost. This becomes of course more and more 
difficult the longer the snakes grow.

%files -n kdesnake
%{_kde_bindir}/kdesnake
%{_kde_applicationsdir}/kdesnake.desktop
%{_kde_iconsdir}/hicolor/*/*/kdesnake.*

#-----------------------------------------------------------------------------

%package -n ksquares
Summary:	KSquares: an implementation of the popular paper based game squares
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ksquares
Requires:	kdegames4-core

%description -n ksquares
KSquares is an implementation of the popular paper based game squares. 
You must draw lines to complete squares, the player with the most s
quares wins.

%files -n ksquares
%{_kde_bindir}/ksquares
%{_kde_applicationsdir}/ksquares.desktop
%{_kde_appsdir}/ksquares
%{_kde_datadir}/config.kcfg/ksquares.kcfg
%{_kde_iconsdir}/hicolor/*/apps/ksquares.png
%{_kde_docdir}/*/*/ksquares

#-----------------------------------------------------------------------------

%package -n kfourinline
Summary:	Place 4 pieces in a row
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=kfourinline
Requires:	kdegames4-core

%description -n kfourinline
kfourinline: place 4 pieces in a row

%files -n kfourinline
%{_kde_bindir}/kfourinline
%{_kde_bindir}/kfourinlineproc
%{_kde_applicationsdir}/kfourinline.desktop
%{_kde_appsdir}/kfourinline
%{_kde_docdir}/*/*/kfourinline
%{_kde_iconsdir}/hicolor/*/apps/kfourinline.png
%{_kde_datadir}/config.kcfg/kwin4.kcfg

#-----------------------------------------------------------------------------

%package -n lskat
Summary:	Lieutnant skat
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=lskat
Requires:	kdegames4-core

%description -n lskat
lskat: lieutnant skat

%files -n lskat
%{_kde_bindir}/lskat
%{_kde_applicationsdir}/lskat.desktop
%{_kde_appsdir}/lskat
%{_kde_docdir}/*/*/lskat
%{_kde_iconsdir}/hicolor/*/apps/lskat.png

#-----------------------------------------------------------------------------

%package -n kdiamond
Summary:	Three-in-a-row game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kdiamond
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE 4 desktop.

%files -n kdiamond
%{_kde_bindir}/kdiamond
%{_kde_applicationsdir}/kdiamond.desktop
%{_kde_appsdir}/kdiamond
%{_kde_configdir}/kdiamond.knsrc
%{_kde_iconsdir}/*/*/*/kdiamond.*
%{_kde_docdir}/*/*/kdiamond
%{_kde_datadir}/sounds/KDiamond*

#-----------------------------------------------------------------------------

%package -n kollision
Summary:	A simple ball dodging game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kollision
A simple ball dodging game

%files -n kollision
%{_kde_bindir}/kollision
%{_kde_applicationsdir}/kollision.desktop
%{_kde_appsdir}/kollision
%{_kde_iconsdir}/*/*/apps/kollision.*
%{_kde_docdir}/*/*/kollision

#-----------------------------------------------------------------------------

%package -n kubrick
Summary:	Game based on Rubik's Cube
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kubrick
Kubrick, a game based on Rubik's Cube

%files -n kubrick
%{_kde_bindir}/kubrick
%{_kde_applicationsdir}/kubrick.desktop
%{_kde_appsdir}/kubrick
%{_kde_docdir}/*/*/kubrick
%{_kde_iconsdir}/hicolor/*/apps/kubrick.png

#-----------------------------------------------------------------------------

%package -n kblocks
Summary:	Single player falling blocks puzzle game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kblocks
Single player falling blocks puzzle game

%files -n kblocks
%{_kde_bindir}/kblocks
%{_kde_applicationsdir}/kblocks.desktop
%{_kde_appsdir}/kblocks
%{_kde_datadir}/config.kcfg/kblocks.kcfg
%{_kde_configdir}/kblocks.knsrc
%{_kde_docdir}/HTML/en/kblocks
%{_kde_iconsdir}/hicolor/*/apps/kblocks.*

#-----------------------------------------------------------------------------

%package -n kbreakout
Summary:	kbreakout
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n kbreakout
Single player falling blocks puzzle game

%files -n kbreakout
%{_kde_bindir}/kbreakout
%{_kde_applicationsdir}/kbreakout.desktop
%{_kde_appsdir}/kbreakout
%{_kde_iconsdir}/hicolor/*/apps/kbreakout.png
%{_kde_docdir}/*/*/kbreakout

#-----------------------------------------------------------------------------

%package -n bomber
Summary:	Arcade bombing game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n bomber
Arcade bombing game

%files -n bomber
%{_kde_bindir}/bomber
%{_kde_applicationsdir}/bomber.desktop
%{_kde_appsdir}/bomber
%{_kde_datadir}/config.kcfg/bomber.kcfg
%{_kde_docdir}/HTML/en/bomber
%{_kde_iconsdir}/hicolor/*/apps/bomber.*

#-----------------------------------------------------------------------------

%package -n ksirk
Summary:	Computerized version of a well known strategy board game
Group:		Graphical desktop/KDE
URL:		http://games.kde.org/game.php?game=ksirk
Requires:	kdegames4-core

%description -n ksirk
KsirK is a computerized version of a well known strategy board game.
KsirK is a multi-player network-playable game with an AI. The goal
of the game is simply to conquer the World... It is done by attacking
your neighbours with your armies.

%files -n ksirk
%{_kde_bindir}/ksirk*
%{_kde_applicationsdir}/ksirk*.desktop
%{_kde_datadir}/config.kcfg/ksirk*settings.kcfg
%{_kde_configdir}/ksirk.knsrc
%{_kde_appsdir}/ksirk*
%{_kde_iconsdir}/*/*/apps/ksirk.png
%{_kde_docdir}/*/*/ksirk
%{_kde_docdir}/*/*/ksirkskineditor

#-----------------------------------------------------------------------------

%package -n granatier
Summary:	KDE Bomberman game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n granatier
KDE Bomberman game.

%files -n granatier
%{_kde_bindir}/granatier
%{_kde_applicationsdir}/granatier.desktop
%{_kde_appsdir}/granatier
%{_kde_datadir}/config.kcfg/granatier.kcfg
%{_kde_docdir}/*/*/granatier
%{_kde_iconsdir}/*/*/apps/granatier.*

#-----------------------------------------------------------------------------

%package -n kigo
Summary:	Go board game for KDE
Group:		Graphical desktop/KDE
Requires:	kdegames4-core
Requires:	gnugo

%description -n kigo
Go board game for KDE.

%files -n kigo
%{_kde_bindir}/kigo
%{_kde_applicationsdir}/kigo.desktop
%{_kde_appsdir}/kigo
%{_kde_datadir}/config.kcfg/kigo.kcfg
%{_kde_configdir}/kigo-games.knsrc
%{_kde_configdir}/kigo.knsrc
%{_kde_docdir}/HTML/en/kigo
%{_kde_iconsdir}/*/*/apps/kigo.png

#-----------------------------------------------------------------------------

%package -n palapeli
Summary:	Jigsaw puzzle game
Group:		Graphical desktop/KDE
Requires:	kdegames4-core

%description -n palapeli
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you
are not limited to aligning pieces on imaginary grids. The pieces are
freely moveable. Also, Palapeli features real persistency, i.e. everything
you do is saved on your disk immediately.

%files -n palapeli
%{_kde_bindir}/palapeli
%{_kde_libdir}/kde4/palapeli_jigsawslicer.so
%{_kde_libdir}/kde4/palapeli_rectslicer.so
%{_kde_libdir}/kde4/palathumbcreator.so
%{_kde_libdir}/kde4/palapeli_goldbergslicer.so
%{_kde_applicationsdir}/palapeli.desktop
%{_kde_appsdir}/palapeli
%{_kde_iconsdir}/hicolor/*/*/*palapeli*
%{_kde_services}/ServiceMenus/palapeli_servicemenu.desktop
%{_kde_services}/palapeli_goldbergslicer.desktop
%{_kde_services}/palapeli_jigsawslicer.desktop
%{_kde_services}/palapeli_rectslicer.desktop
%{_kde_services}/palathumbcreator.desktop
%{_kde_servicetypes}/libpala-slicerplugin.desktop
%{_kde_datadir}/mime/packages/palapeli-mimetypes.xml
%{_kde_configdir}/palapeli-collectionrc
%{_kde_docdir}/HTML/en/palapeli

#-----------------------------------------------------------------------------

%define kdegames_major 6
%define libkdegames %mklibname kdegames %{kdegames_major}

%package -n %{libkdegames}
Summary:	KDE 4 library
Group:		System/Libraries
Obsoletes:	%{mklibname kdegames 4} < %{EVRD}
Obsoletes:	%{mklibname kdegames 5} < %{EVRD}
Obsoletes:	%{mklibname kggzgames 4} < %{EVRD}
Obsoletes:	%{mklibname kggzmod 4} < %{EVRD}
Obsoletes:	%{mklibname kggznet 4} < %{EVRD}

%description -n %{libkdegames}
KDE 4 library.

%files -n %{libkdegames}
%{_kde_libdir}/libkdegames.so.%{kdegames_major}*

#-----------------------------------------------------------------------------

%define kdegamesprivate_major 1
%define libkdegamesprivate %mklibname kdegamesprivate %{kdegamesprivate_major}

%package -n %{libkdegamesprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkdegamesprivate}
KDE 4 library.

%files -n %{libkdegamesprivate}
%{_kde_libdir}/libkdegamesprivate.so.%{kdegamesprivate_major}*

#-----------------------------------------------------------------------------

%define kmahjongglib_major 4
%define libkmahjongglib %mklibname kmahjongglib %{kmahjongglib_major}

%package -n %{libkmahjongglib}
Summary:	KDE 4 library
Group:		System/Libraries
Requires:	kmahjongglib = %{EVRD}

%description -n %{libkmahjongglib}
KDE 4 library.

%files -n %{libkmahjongglib}
%{_kde_libdir}/libkmahjongglib.so.%{kmahjongglib_major}*

#-----------------------------------------------------------------------------

%define kolfprivate_major 4
%define libkolfprivate %mklibname kolfprivate %{kolfprivate_major}

%package -n %{libkolfprivate}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libkolfprivate}
KDE 4 library.

%files -n %{libkolfprivate}
%{_kde_libdir}/libkolfprivate.so.%{kolfprivate_major}*

#-----------------------------------------------------------------------------

%define iris_ksirk_major 2
%define libiris_ksirk %mklibname iris_ksirk %{iris_ksirk_major}

%package -n %{libiris_ksirk}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libiris_ksirk}
KDE 4 library.

%files -n %{libiris_ksirk}
%{_kde_libdir}/libiris_ksirk.so.%{iris_ksirk_major}*

#-----------------------------------------------------------------------------

%define pala_major 0
%define libpala %mklibname pala %{pala_major}

%package -n %{libpala}
Summary:	KDE 4 library
Group:		System/Libraries

%description -n %{libpala}
KDE 4 library.

%files -n %{libpala}
%{_kde_libdir}/libpala.so.%{pala_major}*

#-----------------------------------------------------------------------------

%package devel
Summary:	Headers files for kdegames
Group:		Development/KDE and Qt
Requires:	kdelibs4-devel
Requires:	%{libkdegames} = %{EVRD}
Requires:	%{libkdegamesprivate} = %{EVRD}
Requires:	%{libkmahjongglib} = %{EVRD}
Requires:	%{libkolfprivate} = %{EVRD}
Requires:	%{libiris_ksirk} = %{EVRD}
Requires:	%{libpala} = %{EVRD}

%description devel
Headers files needed to build applications based on kdegames applications.

%files devel
%{_kde_libdir}/cmake/KDEGames
%{_kde_libdir}/libpala/libpala-config.cmake
%{_kde_libdir}/libpala/pala-targets*.cmake
%{_kde_libdir}/libiris_ksirk.so
%{_kde_libdir}/libkdegames.so
%{_kde_libdir}/libkdegamesprivate.so
%{_kde_libdir}/libkmahjongglib.so
%{_kde_libdir}/libkolfprivate.so
%{_kde_libdir}/libpala.so
%{_kde_includedir}/*

#-----------------------------------------------------------------------------

%prep
%setup -q -n kdegames-%{version}
#patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2
- Build without l10n-ru patch for now

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Mon Aug 06 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0
- Update files

* Mon Jul 16 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97
- Make better usage of KDE4 path macros
- Add control over library majors
- Convert BuildRequires to pkgconfig style
- Add pkgconfig(sndfile) to BuildRequires
- Re-diff and enable l10n-ru patch

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Tue Jun 26 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Update to 4.8.90
- Drop no longer needed Conflicts and Obsoletes
- Minor cleanups
- Disable patch (needs re-diff)

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.80-69.1mib2010.2
- New version 4.8.80 (aka 4.9 beta1), we use it because many KDE4 4.8.x games
  don't work well with phonon-gstreamer 4.6
- New libkdegames major (5->6)
- Drop all ggz related stuff
- Add libkdegamesprivate subpackage and library
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 1:4.8.0-69.1mib2010.2
+ Revision: 762514
- Backport to 2010.2 for MIB users
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.8.0-1
+ Revision: 762514
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.97-1
+ Revision: 758099
- New upstream tarball

* Tue Jan 03 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.95-1
+ Revision: 750412
- New version

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.7.90-2
+ Revision: 744329
- Disable buggy rpm5 *feature*
- Fix file list
- Fix file list
- Fix BR
- New upstream tarball
- New upstream tarball 4.7.80
- New version 4.7.41
- Remove branch switch

* Mon Jun 13 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.4-1
+ Revision: 684404
- New version 4.6.4

* Fri May 13 2011 Funda Wang <fwang@mandriva.org> 1:4.6.3-1
+ Revision: 674022
- new version 4.6.3

* Tue Apr 05 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.2-1
+ Revision: 650772
- Remove mkrel
- New version 4.6.2

* Mon Feb 28 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.1-1
+ Revision: 640726
- New version 4.6.1

* Wed Jan 26 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.6.0-1
+ Revision: 632964
- New version KDE 4.6 Final

* Thu Jan 06 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.95-1mdv2011.0
+ Revision: 629120
- New version KDE 4.6 RC2

* Thu Dec 23 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.90-1mdv2011.0
+ Revision: 624062
- New upstream tarball

* Wed Dec 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.85-1mdv2011.0
+ Revision: 616343
- New upstream tarball

* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 1:4.5.80-1mdv2011.0
+ Revision: 601635
- new version 4.5.80 (aka 4.6 beta1)

* Sat Nov 20 2010 Funda Wang <fwang@mandriva.org> 1:4.5.77-0.svn1198704.1mdv2011.0
+ Revision: 599252
- update file list
- new snapshot 4.5.77

* Tue Nov 02 2010 Funda Wang <fwang@mandriva.org> 1:4.5.74-0.svn1192115.1mdv2011.0
+ Revision: 591858
- add sqlite3 as BR for kajongg
- more requires
- add more requires
- new snapshot 4.5.74

* Mon Oct 18 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1184269.3mdv2011.0
+ Revision: 586556
- the correct place for kcardgame is kpat sub package

* Mon Oct 18 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1184269.2mdv2011.0
+ Revision: 586555
- libkcardgame.so is not a devel file

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1:4.5.71-0.svn1184269.1mdv2011.0
+ Revision: 585259
- update file list
- new snapshot

* Thu Sep 16 2010 Funda Wang <fwang@mandriva.org> 1:4.5.68-1mdv2011.0
+ Revision: 578800
- new snapshot 4.5.68

* Tue Sep 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.67-1mdv2011.0
+ Revision: 576503
- Fix file list
- New version 4.5.67

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.5.0-1mdv2011.0
+ Revision: 566568
- New upstream tarball
- Update to version 4.5.0

* Thu Jul 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.95-1mdv2011.0
+ Revision: 562877
- Fix file list
- Add buildrequires
- KDE 4.5 RC3

* Thu Jul 15 2010 Anssi Hannula <anssi@mandriva.org> 1:4.4.3-3mdv2011.0
+ Revision: 553774
- fix conflicts in bovo package

* Wed May 26 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-2mdv2010.1
+ Revision: 546159
- Rebuild in release mode

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.3-1mdv2010.1
+ Revision: 542101
- Update to version 4.4.3
- Fix devel package file list

* Wed Mar 31 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.2-1mdv2010.1
+ Revision: 530115
- Fix file list
- Update to version 4.4.2

* Tue Mar 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.1-1mdv2010.1
+ Revision: 513408
- Update to version 4.4.1

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.4.0-1mdv2010.1
+ Revision: 502610
- Update to version 4.4.0

* Mon Feb 01 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.98-1mdv2010.1
+ Revision: 498943
- Update to version 4.3.98 aka "kde 4.4 RC3"
- Update to version 4.3.98 aka "kde 4.4 RC3"

* Mon Jan 25 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.95-1mdv2010.1
+ Revision: 495992
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Update to version 4.3.95 aka "kde 4.4 RC2"
- Remove the cp trick as the icons belong to an other package
- Add missing icons in hicolor

* Sun Jan 10 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.90-1mdv2010.1
+ Revision: 488618
- Fix file list
- Fix file list
- Update to kde 4.4 rc1

* Mon Dec 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.85-1mdv2010.1
+ Revision: 480818
- Fix file list
- Update to kde 4.4 beta2
  Remove merged patches
  Remove old unneded Buildrequires
- Add Gnugo as Requires for Kigo

* Sat Dec 05 2009 Funda Wang <fwang@mandriva.org> 1:4.3.80-1mdv2010.1
+ Revision: 473680
- finally fix building
- add palapeli
- bump versioned requires

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix version in BuildRequires
    - Update to kde 4.4 beta1

* Sat Nov 28 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.77-1mdv2010.1
+ Revision: 470788
- Add branch switch
- Fix typo in suggests

  + Funda Wang <fwang@mandriva.org>
    - New version 4.3.77

* Fri Nov 20 2009 Funda Wang <fwang@mandriva.org> 1:4.3.75-1mdv2010.1
+ Revision: 467591
- New version 4.3.75

* Wed Nov 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-2mdv2010.1
+ Revision: 465070
- Rebuild against new qt

* Sun Nov 08 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.73-1mdv2010.1
+ Revision: 463213
- Update to kde 4.3.73

* Tue Oct 06 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.2-1mdv2010.0
+ Revision: 454660
- New upstream release 4.3.2.

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 1:4.3.1-4mdv2010.0
+ Revision: 453846
- BUMP rel
- singled out kmahjongglib as required by all mahjongg-like games.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix typo

* Sun Sep 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.1-2mdv2010.0
+ Revision: 438584
- Obsolete kde3 packages

* Tue Sep 01 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.1-1mdv2010.0
+ Revision: 423217
- New upstream release 4.3.1.

* Fri Aug 21 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.3.0-2mdv2010.0
+ Revision: 418983
- Rebuild for missing package
- Change requires into suggests
  Fix Ksirk summary

* Tue Aug 04 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.3.0-1mdv2010.0
+ Revision: 409416
- New upstream release 4.3.0.
- Update to KDE 4.3 RC3

* Sat Jul 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.96-1mdv2010.0
+ Revision: 394895
- Update to Rc2

* Sat Jun 27 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-2mdv2010.0
+ Revision: 389795
- Fix conflicts

* Fri Jun 26 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.95-1mdv2010.0
+ Revision: 389391
- Update to kde 4.3Rc1

* Thu Jun 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.90-1mdv2010.0
+ Revision: 382854
- Remove merged patches
- Update to beta2

* Fri May 29 2009 Funda Wang <fwang@mandriva.org> 1:4.2.88-1mdv2010.0
+ Revision: 380796
- fix file list
- New version 4.2.88

* Fri May 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.87-1mdv2010.0
+ Revision: 378822
- Update to kde   4.2.87

* Sat May 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.85-1mdv2010.0
+ Revision: 373564
- Update to kde 4.2.85
- Update to kde 4.2.85

* Sun May 03 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.71-0.svn961800.1mdv2010.0
+ Revision: 371234
- Update to kde 4.2.71

* Sat May 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.70-0.svn954171.1mdv2010.0
+ Revision: 370697
- Update to kde 4.2.70
  Add Ktron and Kdesnake
  Fix file list

* Sun Apr 05 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.2-3mdv2009.1
+ Revision: 364187
- Add some upstream patches from branch
        - Patch100: Kubrik : missing opengl include
- Remove Old tarball
  Fix crash in Ksirk at server connect (BKO: 187235 QMO: 49132)

* Fri Mar 27 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.2-1mdv2009.1
+ Revision: 361727
- Update with 4.2.2 try#1 packages

* Sat Feb 28 2009 Helio Chissini de Castro <helio@mandriva.com> 1:4.2.1-1mdv2009.1
+ Revision: 346212
- KDE 4.2.1 try#1 upstream release

* Mon Feb 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.2.0-2mdv2009.1
+ Revision: 340881
- Rebuild against qt4.5
- Fix bomber description

* Wed Jan 28 2009 Funda Wang <fwang@mandriva.org> 1:4.2.0-1mdv2009.1
+ Revision: 334820
- New version 4.2.0

* Fri Jan 09 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.96-1mdv2009.1
+ Revision: 327304
- Fix file list

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Release Candidate 1 - 4.1.96

* Sun Dec 14 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.85-1mdv2009.1
+ Revision: 314060
- New version KDE 4.2 Beta2

* Thu Dec 11 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.82-1mdv2009.1
+ Revision: 313374
- Update to kde 4.1.82

* Mon Dec 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.81-2mdv2009.1
+ Revision: 308661
- Rebuild

* Sun Nov 30 2008 Funda Wang <fwang@mandriva.org> 1:4.1.81-1mdv2009.1
+ Revision: 308426
- New version 4.1.81
- drop ksudoku build condition

* Wed Nov 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-3mdv2009.1
+ Revision: 306997
- Versionnate Obsoletes

* Tue Nov 25 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-2mdv2009.1
+ Revision: 306582
- some more obsoletes
- Obsoletes kdegames

  + Funda Wang <fwang@mandriva.org>
    - requires new game

* Thu Nov 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.80-1mdv2009.1
+ Revision: 304864
- New subpackage Bomber

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with Beta 1 - 4.1.80

* Mon Nov 17 2008 Funda Wang <fwang@mandriva.org> 1:4.1.73-2mdv2009.1
+ Revision: 303889
- add patch fixing ksudoku build

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.1.73-1mdv2009.1
+ Revision: 303397
- Fix BuildRequires
- Update to kde 4.1.73
- Fix Requires on core package

* Sun Oct 26 2008 Funda Wang <fwang@mandriva.org> 1:4.1.71-1mdv2009.1
+ Revision: 297352
- install kapman.desktop into correct dir
- require two new games
- update file list
- New version 4.1.71

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 1:4.1.2-3mdv2009.1
+ Revision: 292759
- move devel package section so that all the libs are declared
- fix wrong .so suffix of libkdegames
- devel package should requires libpackages

* Thu Oct 02 2008 Frederic Crozat <fcrozat@mandriva.com> 1:4.1.2-2mdv2009.0
+ Revision: 290841
- Add conflicts to ease upgrade

* Thu Sep 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.2-1mdv2009.0
+ Revision: 288309
- KDE 4.1.2 arriving.

* Sun Aug 31 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.1-1mdv2009.0
+ Revision: 277839
- Upgrade to forthcoming 4.1.1 packages

  + Funda Wang <fwang@mandriva.org>
    - update url

* Fri Jul 25 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.1.0-1mdv2009.0
+ Revision: 247585
- Update with Release Candidate 1 - 4.1.0

* Thu Jul 10 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.98-1mdv2009.0
+ Revision: 233190
- Update with Release Candidate 1 - 4.0.98

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.85-1mdv2009.0
+ Revision: 232461
- New version kde 4.0.85

* Sun Jun 29 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.84-2mdv2009.0
+ Revision: 229949
- Underlinnk patch was included upstream
- Fix br
- Update with new snapshot tarballs 4.0.84

* Mon Jun 23 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.83-2mdv2009.0
+ Revision: 228415
- Enabled ggz back, wrongly removed based on bad freeciv packaging.
- Commented ksudoku for now, since underlinking issue is happening upstream
- Added reference for proper ggz packaging, should discuss later with mdv staff best method to package mosules stuff
- Update with new snapshot tarballs 4.0.83
- Update with new snapshot tarballs 4.0.82

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.81-1mdv2009.0
+ Revision: 214719
- Update with new snapshot tarballs 4.0.81

* Sat May 24 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.80-1mdv2009.0
+ Revision: 210783
- New upstream kde4 4.1 beta1

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Own %%{_kde_appsdir}/kmahjongglib
    - Own better the folders

* Mon May 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-4mdv2009.0
+ Revision: 209203
- Remove description about kbackgammon
  Obsolete old kde4-kbackgammon

* Fri May 16 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.74-3mdv2009.0
+ Revision: 208266
- Rebuild against new kdebase4
- Versionate BuildRequires

* Fri May 16 2008 Funda Wang <fwang@mandriva.org> 1:4.0.74-2mdv2009.0
+ Revision: 208038
- New version 4.0.74

* Fri May 09 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.73-2mdv2009.0
+ Revision: 204789
- Say hello to kbreakout and ksirk
  Remove ggz-lib buildrequires and add a comment about that

* Wed May 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.72-2mdv2009.0
+ Revision: 202770
- Fix BuildRequires
- Update to kde 4.0.72
- Add new subpackage +> KBlocks
  Fix file list
  Fix provides ( copy / paste suxx )
- Fix Requires
- New sub packages kubrick kollision and kdiamond
  Fix File list
- New snapshot 4.0.69

  + Helio Chissini de Castro <helio@mandriva.com>
    - New upstream kde4 4.1 alpha 1

* Fri Mar 28 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.3-1mdv2008.1
+ Revision: 191003
- Update for last stable release 4.0.3

* Sat Mar 08 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:4.0.2-2mdv2008.1
+ Revision: 182263
- Rebuild against new qt4 changes

* Sat Mar 01 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.2-1mdv2008.1
+ Revision: 177437
- New upstream bugfix release 4.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - fix spacing at top of description

* Tue Feb 12 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.1-1mdv2008.1
+ Revision: 165897
- Update for 4.0.1

* Wed Jan 09 2008 Helio Chissini de Castro <helio@mandriva.com> 1:4.0.0-1mdv2008.1
+ Revision: 147335
- Updated to latest 4.0.0 stable

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New snapshot
      Kwin4 is now called Kfourinline

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Dec 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.97.1-0.746784.1mdv2008.1
+ Revision: 117087
- New snapshot
  Obsolete libkolflib on libkolfprivate packag

* Fri Nov 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.742894.1mdv2008.1
+ Revision: 114116
- New snapshot

* Fri Nov 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.1-0.740193.1mdv2008.1
+ Revision: 111553
- New snapshot
  Package kcfg files in there own  package ( Bug #35626)

* Sat Nov 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.96.0-0.737137.1mdv2008.1
+ Revision: 109648
- KDE4 RC1

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.2-0.734589.2mdv2008.1
+ Revision: 107542
- Fix Requires

* Sun Nov 11 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.2-0.734589.1mdv2008.1
+ Revision: 107536
- New snapshot
  kbackgammon is not on the package anymore

* Fri Nov 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.95.1-0.731582.1mdv2008.1
+ Revision: 104988
- New snapshot post Rc1

* Tue Oct 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.730797.1mdv2008.1
+ Revision: 103774
- Fix File list
- New snashot

* Thu Oct 25 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.1-0.729193.1mdv2008.1
+ Revision: 102157
- New snapshot

* Sat Oct 20 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.94.0-0.727095.1mdv2008.1
+ Revision: 100515
- Kde 4 Beta 3

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-ended-with-dot

* Fri Sep 21 2007 Tiago Salem <salem@mandriva.com.br> 1:3.93.0-0.714146.1mdv2008.0
+ Revision: 91944
- Changing Obsoletes tags and updating tarball to a newer revision.

  + Helio Chissini de Castro <helio@mandriva.com>
    - Update with revision 711178

* Tue Sep 04 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.93.0-0.707981.1mdv2008.0
+ Revision: 79000
- Update with revision 707981
- Update with revision 706624

* Thu Aug 30 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.706247.1mdv2008.0
+ Revision: 75096
- Update with revision 706247

* Wed Aug 29 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.705994.1mdv2008.0
+ Revision: 73335
- Update with revision 705994

* Mon Aug 06 2007 Helio Chissini de Castro <helio@mandriva.com> 1:3.92.0-0.696866.1mdv2008.0
+ Revision: 59504
- UPdate to revision 696866
- Update to revision 693322

* Wed Jul 04 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.682394.2mdv2008.0
+ Revision: 48038
- New snapshot post monday BIC
- Fix main package and the -core one

* Sat Jun 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:3.91-0.681524.1mdv2008.0
+ Revision: 46068
- Fix File list
- Start to fix file list to satisfy new kde layout

* Thu May 10 2007 Laurent Montel <lmontel@mandriva.org> 1:3.90.1-0.20070502.1mdv2008.0
+ Revision: 25996
- new snapshot

* Fri May 04 2007 Laurent Montel <lmontel@mandriva.org> 1:3.80.3-0.20070502.3mdv2008.0
+ Revision: 22301
- new snapshot
- new snapshot


* Sun Mar 11 2007 Laurent Montel <lmontel@mandriva.com> 3.80.3-0.20070311.3mdv2007.1
+ Revision: 141383
- new snapshot
- Fix spec file
- new snapshot
- new snapshot
- 3.80.3
- new snapshot

* Tue Jan 23 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070123.2mdv2007.1
+ Revision: 112289
- new snapshot

* Thu Jan 18 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070117.2mdv2007.1
+ Revision: 110236
- Update

* Wed Jan 10 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070109.2mdv2007.1
+ Revision: 107028
- Increase version because bot rebuild is stupid
- Update snapshot

* Wed Jan 03 2007 Laurent Montel <lmontel@mandriva.com> 1:3.80.2-0.20070103.1mdv2007.1
+ Revision: 103686
- Fix spec file
- Update
- Byebye menu macro

* Thu Dec 28 2006 Laurent Montel <lmontel@mandriva.com> 1:3.80-3mdv2007.1
+ Revision: 102279
- Import kdegames4

* Fri Nov 03 2006 Laurent Montel <lmontel@mandriva.com> 3.5.5-3mdv2007.0
- First package

