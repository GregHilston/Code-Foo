<?php

class Rule
{
    public $color;
    public $must = [];
    public $must_not = [];

    public function testCut($color)
    {
        return (count($this->must) == 0 || in_array($color, $this->must)) && !in_array($color, $this->must_not);
    }

    public static function convertFromStdClass(stdClass $input)
    {
        $instance = new static;
        
        foreach (get_object_vars($input) as $key => $value) {
            $instance->$key = $value;
        }

        return $instance;
    }
}

class RuleSet
{
    protected $rules = [];

    public function add(Rule $rule)
    {
        $this->rules[$rule->color][] = $rule;
    }

    public function testCut($color, $previousColor = null)
    {
        if (!is_null($previousColor) && array_key_exists($previousColor, $this->rules)) {
            foreach ($this->rules[$previousColor] as $rule) {
                if (!$rule->testCut($color)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static function buildFromArray(array $input)
    {
        $instance = new static;
        foreach ($input as $ruleDefinition) {
            $rule = Rule::convertFromStdClass($ruleDefinition);
            $instance->add($rule);
        }

        return $instance;
    }
}

$rulesetDefinition = json_decode(file_get_contents($argv[1]));
$ruleset = RuleSet::buildFromArray($rulesetDefinition);

echo "Tick tick... ";

$previousColor = null;
while ($color = fgets(STDIN)) {
    $color = trim($color);
    if (!$ruleset->testCut($color, $previousColor)) {
        echo "Boom!\n";
        exit();
    }
    $previousColor = $color;
}
echo "Whew!\n";