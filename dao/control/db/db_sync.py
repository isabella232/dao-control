# # -*- encoding: utf-8 -*-
# #
# # Copyright 2013 Hewlett-Packard Development Company, L.P.
# # Copyright 2016 Symantec.
# # All Rights Reserved.
# #
# #    Licensed under the Apache License, Version 2.0 (the "License"); you may
# #    not use this file except in compliance with the License. You may obtain
# #    a copy of the License at
# #
# #         http://www.apache.org/licenses/LICENSE-2.0
# #
# #    Unless required by applicable law or agreed to in writing, software
# #    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# #    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# #    License for the specific language governing permissions and limitations
# #    under the License.
#
# """
# Run storage database migration.
# """
#
# import sys
#
# from dao.control.db import migration
#
#
# class DBCommand(object):
#
#     def upgrade(self, revision):
#         migration.upgrade(revision)
#
#     def downgrade(self, revision):
#         migration.downgrade(revision)
#
#     def revision(self, message, autogenerate):
#         migration.revision(message, autogenerate)
#
#     def stamp(self, revision):
#         migration.stamp(revision)
#
#     def version(self):
#         print(migration.version())
#
#     def create_schema(self):
#         migration.create_schema()
