#pragma once

namespace Test {

    /*!
     * \brief class to add numbers
     *
     * \tparam T type of numbers
     */
    template <typename T>
    class Adder {
    private:
        //! total number
        T _total;

    public:
        /*!
         * \brief default constructor
         *
         * This makes the total number to be zero
         */
        Adder() : _total(T(0)) {}

        /*!
         * \brief add a number
         *
         * \param number added number
         */
        void add(T number) { _total += number; }

        /*!
         * \brief get the total number
         *
         * \return T total number
         */
        T total() const { return _total; }
    };

}  // namespace Test
