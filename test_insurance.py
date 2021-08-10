import unittest
from client_pages import TickBiteInsurancePolicyForm, City
from helpers import Helper


class TestInsurance(unittest.TestCase):
    def test_tick_bite_insurance_policy(self):
        """Полис страхования от укуса клеща"""
        helper = Helper()

        tick_bite_form = TickBiteInsurancePolicyForm(helper)
        tick_bite_form.open()
        tick_bite_form.choose_insure_persons_count(2)
        tick_bite_form.select_mite()
        tick_bite_form.choose_region(City.krasnodar)
        self.assertEqual(helper.get_field_value(tick_bite_form.promocode_field), '')

        calculate_form = tick_bite_form.calculate()
        calculate_form.check_sum(600)
        self.assertRegex(calculate_form.get_number_text(), '^[0-9]{8}$')

        helper.browser.quit()
