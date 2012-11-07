# workaround bug in rpm unpackaged subdir check
%define _unpackaged_subdirs_terminate_build 0

Name:		kdegames4
Summary:	KDE - Games
Version: 4.9.3
Release: 1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPL
URL:		http://games.kde.org/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdegames-%{version}.tar.xz
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
%{_kde_libdir}/cmake/KDEGames/KDEGamesConfig.cmake
%{_kde_libdir}/cmake/KDEGames/KDEGamesConfigVersion.cmake
%{_kde_libdir}/cmake/KDEGames/KDEGamesLibraryDepends*.cmake
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
#%patch0 -p1

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

