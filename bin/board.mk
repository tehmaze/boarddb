SOURCES := $(wildcard *.yaml)
TARGETS := $(patsubst %.yaml,%.json,$(SOURCES))
BINDIR  := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
BASEDIR := $(abspath $(BINDIR)/..)

BOARD_SCHEMA := $(BASEDIR)/board.schema.json

all: $(TARGETS)

%.json: %.yaml
	$(BINDIR)/board2json.py $< $@.temp && \
	$(BINDIR)/validate.py $(BOARD_SCHEMA) $@.temp && \
	mv $@.temp $@ || $(RM) $@.temp