import streamlit as st
import subprocess

# Define functions to run each program
def simulate_cp_command():
    st.subheader("Simulation of CP Command")
    cp_script = '''
    #!/bin/bash
    cp T1.txt T2.txt
    cat T2.txt
    '''
    st.code(cp_script, language='bash')

def simulate_head_command():
    st.subheader("Simulation of head Command")
    head_script = '''
    #!/bin/sh
    read inp
    head -n "$inp" T3.txt
    '''
    st.code(head_script, language='bash')

def simulate_wc_command():
    st.subheader("Simulation of WC Command")
    wc_script = '''
    #!/bin/sh
    wc T.txt
    '''
    st.code(wc_script, language='bash')

def simulate_grep_command():
    st.subheader("Simulation of grep Command")
    grep_script = '''
    #!/bin/bash
    read pat
    read file
    grep "$pat" "$file"
    '''
    st.code(grep_script, language='bash')

def simulate_tail_command():
    st.subheader("Simulation of tail Command")
    tail_script = '''
    #!/bin/sh
    read inp
    tail -n "$inp" T4.txt
    '''
    st.code(tail_script, language='bash')

def calculator_program():
    st.subheader("Calculator Program")
    calc_script = '''
    #!/bin/bash

    read a
    read c
    read b 

    case $c in
        '+') echo "The sum is  $((a+b)) " ;; 
        '-') echo "The difference is $((a-b))" ;;
        '*') echo "The product is $((a*b))" ;;
        '/') echo "The quotient is $((a/b))" ;;
        '%') echo "The remainder is $((a%b))" ;;
        *) echo "Invalid Input" ;;
    esac
    '''
    st.code(calc_script, language='bash')

def prime_numbers_program():
    st.subheader("Prime Numbers Program")
    prime_script = '''
    #!/bin/bash

    # Function to check if a number is prime
    is_prime(){
        num=$1
        if ((num <= 1)); then
            return 1
        fi
        if ((num <= 3)); then
            return 0
        fi
        if ((num % 2 == 0)) || ((num % 3 == 0)); then 
            return 1
        fi
        i=5
        while ((i * i <= num)); do
            if ((num % i == 0)) || ((num % (i + 2) == 0)); then 
                return 1
            fi
            i=$((i + 6))
        done 
        return 0
    }

    # Function to generate the series
    generate_series(){
        n=$1
        count=0
        num=2
        while ((count < n)); do
            if is_prime "$num"; then
                echo -n "$num "
                count=$((count + 1))
            fi
            num=$((num + 1))
        done    
    }

    # Input
    read -p "Enter the number of terms: " n

    # Generate and print series
    generate_series "$n"
    echo
    '''
    st.code(prime_script, language='bash')

def system_wait_call_program():
    st.subheader("System Wait Call Program")
    wait_script = '''
    #!/bin/bash

    print_numbers(){
        prefix="$1"
        starts="$2"
        ends="$3"
        echo -n "$prefix"
        i="$starts"
        while [ $i -le $ends ]; do
            echo -n "$i "
            i=$((i+2))
        done
        echo ""
    }

    child_process(){
        echo "Child starts"
        print_numbers "Odd Nos:" 1 9
        echo "Child ends"
    }

    parent_process(){
        echo "Parent starts"
        print_numbers "Even Nos:" 2 10
        echo "Parent ends"
    }

    child_process &
    wait  # Wait for child process to complete
    parent_process
    '''
    st.code(wait_script, language='bash')

# Main Streamlit app
def main():
    st.title('Simulation of Git Bash Programs')

    st.sidebar.title('Select a Program')
    program_choice = st.sidebar.selectbox(
        'Choose a program to simulate:',
        ['CP Command', 'Head Command', 'WC Command', 'Grep Command', 'Tail Command',
         'Calculator Program', 'Prime Numbers Program', 'System Wait Call Program']
    )

    if program_choice == 'CP Command':
        simulate_cp_command()
    elif program_choice == 'Head Command':
        simulate_head_command()
    elif program_choice == 'WC Command':
        simulate_wc_command()
    elif program_choice == 'Grep Command':
        simulate_grep_command()
    elif program_choice == 'Tail Command':
        simulate_tail_command()
    elif program_choice == 'Calculator Program':
        calculator_program()
    elif program_choice == 'Prime Numbers Program':
        prime_numbers_program()
    elif program_choice == 'System Wait Call Program':
        system_wait_call_program()

if __name__ == '__main__':
    main()
