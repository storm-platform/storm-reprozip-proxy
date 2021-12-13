#
# Copyright (C) 2021 Storm Project.
#
# storm-job-reana is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

FROM stormproject/storm-reprozip-base:latest

#
# Copy files
#
COPY docker/proxy/tools/proxy.sh /proxy.sh

#
# Configure container execution
#
CMD ["/proxy.sh"]
