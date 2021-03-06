# This file is part of mazespace.
#
# mazespace is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# mazespace is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with mazespace.  If not, see <http://www.gnu.org/licenses/>.
#


from flask import *
from mazespace import mazespace






@mazespace.route("/")
def index():
    return render_template('index.html', main_wall_title='MAIN WALL', right_wall_title='RIGHT WALL', left_wall_title='LEFT WALL')

