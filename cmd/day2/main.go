package main

import (
	"advent-of-code-2021/internal/converters"
	"advent-of-code-2021/internal/files"
	"log"
	"strings"
)

type Submarine struct {
	horizontal int
	depth      int
	aim        int
	commands   map[string]SubmarineCommand
}

func (s *Submarine) Execute(command string) error {
	sp := strings.Split(command, " ")
	num, err := converters.StringToInt(sp[1])
	if err != nil {
		return err
	}

	s.commands[sp[0]](s, num)

	return nil
}

func (s *Submarine) MultiplyHorizontalByDepth() int {
	return s.horizontal * s.depth
}

type SubmarineCommand func(s *Submarine, n int)

func ForwardCommand(s *Submarine, n int) {
	s.horizontal += n
}

func DiveCommand(s *Submarine, n int) {
	s.depth += n
}

func SurfaceCommand(s *Submarine, n int) {
	s.depth -= n
}

func ForwardAimcommand(s *Submarine, n int) {
	s.horizontal += n
	s.depth += n * s.aim
}

func AimDownCommand(s *Submarine, n int) {
	s.aim += n
}

func AimUpCommand(s *Submarine, n int) {
	s.aim -= n
}

func main() {
	var err error

	defer func() {
		if err != nil {
			log.Fatalf("%+v", err)
		}
	}()

	commands, err := files.Load("cmd/day2/input.txt", "\n")
	if err != nil {
		return
	}

	sub := Submarine{
		commands: map[string]SubmarineCommand{
			"forward": ForwardCommand,
			"down":    DiveCommand,
			"up":      SurfaceCommand,
		},
	}

	for _, c := range commands {
		err = sub.Execute(c)
		if err != nil {
			return
		}
	}
	log.Printf("Part One Answer: %d", sub.MultiplyHorizontalByDepth())

	subAim := Submarine{
		commands: map[string]SubmarineCommand{
			"forward": ForwardAimcommand,
			"down":    AimDownCommand,
			"up":      AimUpCommand,
		},
	}

	for _, c := range commands {
		err = subAim.Execute(c)
		if err != nil {
			return
		}
	}
	log.Printf("Part Two Answer: %d", subAim.MultiplyHorizontalByDepth())
}
