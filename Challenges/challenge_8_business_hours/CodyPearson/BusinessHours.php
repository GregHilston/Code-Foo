<?php

class BusinessDay {
    public $startTime;
    public $endTime;

    public static function toTwelveHour($time)
    {
        list($hour, $minute) = str_split($time, 2);


        $suffix = $hour >= 12 ? 'pm' : 'am';

        if ($hour == 0) {
            $hour = 12;
        } elseif ($hour > 12) {
            $hour -= 12;
        }

        return "$hour:$minute$suffix";
    }

    public function __toString()
    {
        if ($this->startTime == '0000' && $this->endTime == '0000') {
            return '24h';
        } else {
            return sprintf('%s - %s', self::toTwelveHour($this->startTime), self::toTwelveHour($this->endTime));
        }
    }
}

class BusinessHours implements JsonSerializable {
    public static $dayCodes = [
        'N' => 'Sunday',
        'M' => 'Monday',
        'T' => 'Tuesday',
        'W' => 'Wednesday',
        'R' => 'Thursday',
        'F' => 'Friday',
        'S' => 'Saturday'
    ];

    public $openDays;

    public function __construct()
    {
        $dayArray = new ArrayIterator;

        foreach (array_keys(self::$dayCodes) as $shortCode) {
            $dayArray[$shortCode] = new ArrayObject;
        }

        $this->openDays = new InfiniteIterator($dayArray);
    }

    public function addRange($range)
    {
        $components = [];
        $valid = preg_match('/([NMTWRFS])([NMTWRFS])(\d{4})(\d{4})H/', $range, $components);
        if (!$valid) {
            return;
        }

        list(, $startDay, $endDay, $startTime, $endTime) = $components;

        $businessDay = new BusinessDay;
        $businessDay->startTime = $startTime;
        $businessDay->endTime = $endTime;

        $this->openDays->rewind();

        $inRange = false;
        while (true) {
            if ($this->openDays->key() == $startDay) {
                $inRange = true;
            }
            if ($inRange) {
                $this->openDays->current()->append($businessDay);
            }
            if ($this->openDays->key() == $endDay) {
                break;
            }
            $this->openDays->next();
        }
    }

    public function jsonSerialize()
    {
        $output = [];
        $days = $this->openDays->getInnerIterator();
        
        $days->rewind();

        foreach ($days as $dayCode => $openHours) {
            $output[self::$dayCodes[$dayCode]] = implode(', ', $openHours->getArrayCopy());
        }

        return $output;
    }
}

// Test script
$businessHours = new BusinessHours;
while ($line = fgets(STDIN)) {
    $businessHours->addRange($line);
}

echo json_encode($businessHours);