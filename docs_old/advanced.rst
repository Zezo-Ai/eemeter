Advanced Usage
==============

CalTRACK method options
-----------------------

TODO. For now, see :ref:`caltrack` for full set of options.

CalTRACK Data Sufficiency Criteria
----------------------------------

Compute data sufficiency (:any:`eemeter.caltrack_sufficiency_criteria`)::

    >>> data_sufficiency = eemeter.caltrack_sufficiency_criteria(data)


About the CalTRACK methods
--------------------------

The eemeter library is the reference implementation of the CalTRACK methods,
but it is *not* the CalTRACK methods. CalTRACK refers to the methods
themselves, for which the documentation is not kept in this repository.
The most current information about methods and proposed changes can be found
on `github <https://github.com/energy-market-methods/caltrack/>`_.

How the models work
///////////////////

We're planning a deeper dive on the methods here, but for now, see
`openee.io <https://www.openee.io/open-source/how-it-works>`_, dig into
the :ref:`caltrack` (try viewing the source link),
or try :any:`visualizing <eemeter.CalTRACKUsagePerDayModelResults.plot>` some
the models built with the sample data.


For developers
--------------

Contributing
////////////

We highly encourage contributing to eemeter. To contribute, please create an
`issue <http://github.com/openeemeter/eemeter/issues>`_ or a pull request.

Dev installation
////////////////

We use docker for development. To get started with docker, see
`docker installation <https://docs.docker.com/install/>`_.

Fork and clone a local copy of the repository::

    $ git clone git@github.com:YOURUSERNAME/eemeter.git eemeter
    $ cd eemeter
    $ git remote add upstream git://github.com/openeemeter/eemeter.git

Then try one of the following:

Open a jupyter notebook::

    $ docker-compose up jupyter

Build a local version of the docs::

    $ docker-compose up docs

Run the tests::

    $ docker-compose run --rm test

Open up a shell::

    $ docker-compose up shell


Command-line Usage
------------------

Once installed, ``eemeter`` can be run from the command-line. To see all available commands, run ``eemeter --help``.

Use CalTRACK methods on sample data::

    $ eemeter caltrack --sample=il-electricity-cdd-hdd-daily

Save output::

    $ eemeter caltrack --sample=il-electricity-cdd-only-billing_monthly --output-file=/path/to/output.json

Load custom data (see :any:`eemeter.meter_data_from_csv` and :any:`eemeter.temperature_data_from_csv` for formatting)::

    $ eemeter caltrack --meter-file=/path/to/meter/data.csv --temperature-file=/path/to/temperature/data.csv

Do not fit CDD-based candidate models (intended for gas data)::

    $ eemeter caltrack --sample=il-gas-hdd-only-billing_bimonthly --no-fit-cdd

