# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Copyright Commvault Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------

"""File for class PreLogin, class for all pre login tasks.

PreLogin is the only class defined in this file.

PreLogin: Represents pre login tasks, including deletion of old session files and creation of a new session file.

PreLogin:
    clean_up()              --  Logs in to Commcell.
    create_session_file()   --  Create a session file based on the UID of the user executing the script.

"""

import os
import glob
import stat
from time import time

FILE_PATH = os.path.join(os.sep, "tmp", "CVANSIBLE_{SESSION_ID}")
SESSION_ID = os.getuid()


class PreLogin:
    """Class represents pre login tasks, including deletion of old session files and creation of a new session file."""

    @staticmethod
    def clean_up():
        """
        Performs pre-login operations i.e clean up of old session file & creation of new file for current session.
        Returns a file handle to the session file.

            Args:
                N/A

            Returns:
                N/A

            Raises:
                Exception in case the older session files can't be deleted.

        """
        # STEP 1 : TRY TO CLEAN UP ALL STALE SESSION FILES.
        all_session_files = glob.glob(FILE_PATH.format(SESSION_ID="*"))
        for file in all_session_files:
            try:
                if int(time())-int(os.path.getatime(file)) > 86400:
                    os.remove(file)
            except OSError:
                continue

    @staticmethod
    def create_session_file():
        """
        Create a session file based on the UID of the user executing the script and set RWX permissions for owner.

            Args:
                N/A

            Returns:
                obj - handle to session file.

            Raises:
                N/A

        """

        session_file_path = FILE_PATH.format(SESSION_ID=SESSION_ID)
        fh = open(session_file_path, 'wb')
        os.chmod(session_file_path, stat.S_IRWXU)  # SET READ, WRITE & EXECUTE PERMISSIONS FOR OWNER
        return fh
